'''
Created on 14-Aug-2025

@author: jeete
'''
#!/usr/bin/env python3
"""
Interview Practice AI Agent (CLI + Voice)
-----------------------------------------
Adds:
- TTS: AI speaks each question
- STT: You answer verbally and AI transcribes

Setup:
1) pip install --upgrade openai python-dotenv rich sounddevice scipy pydub
2) Install ffmpeg (for pydub)
3) export OPENAI_API_KEY=sk-...
"""

import argparse
import datetime as dt
import json
import os
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict, Any

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()
console = Console()

SUPPORTED_TOPICS = {
    "qa": "QA Automation / SDET",
    "behavioral": "Behavioral / HR",
    "dsa": "Data Structures & Algorithms",
    "devops": "DevOps/SRE",
}

LEVEL_HINTS = {
    "junior": "Focus on fundamentals.",
    "mid": "Balance fundamentals with practical tradeoffs.",
    "senior": "Emphasize architecture, strategy, scalability.",
}

QUESTION_BANK = {
    "qa": [
        {"q": "Walk me through a robust UI automation framework you designed."},
        {"q": "How do you design an API test strategy for microservices?"},
    ],
    "behavioral": [
        {"q": "Describe a conflict with a developer and how you resolved it."},
    ],
}

@dataclass
class SessionConfig:
    topic: str = "qa"
    level: str = "mid"
    rounds: int = 4
    model: str = "gpt-4.1-mini"

@dataclass
class QARecord:
    question: str
    answer: str
    feedback: str
    score: int

class InterviewAgent:
    def __init__(self, cfg: SessionConfig):
        self.cfg = cfg
        self.client = OpenAI()
        self.records: List[QARecord] = []

    def text_to_speech(self, text):
        audio_file = tempfile.mktemp(suffix=".mp3")
        with self.client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=text
        ) as resp:
            with open(audio_file, "wb") as f:
                f.write(resp.read())
        sound = AudioSegment.from_mp3(audio_file)
        play(sound)

    def record_voice(self, duration=30, samplerate=44100):
        console.print(f"🎙️ Speak now ({duration} seconds max)...")
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()
        wav_path = tempfile.mktemp(suffix=".wav")
        write(wav_path, samplerate, (audio_data * 32767).astype(np.int16))
        return wav_path

    def speech_to_text(self, audio_path):
        with open(audio_path, "rb") as f:
            transcript = self.client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=f
            )
        return transcript.text.strip()

    def run(self):
        console.print(Panel.fit(f"Interview Topic: {self.cfg.topic}\nLevel: {self.cfg.level}"))
        questions = QUESTION_BANK.get(self.cfg.topic, [])

        for i in range(self.cfg.rounds):
            q = questions[i % len(questions)]["q"]
            console.rule(f"Question {i+1}")
            console.print(Markdown(f"**Q{i+1}.** {q}"))
            self.text_to_speech(q)

            audio_path = self.record_voice()
            answer = self.speech_to_text(audio_path)
            console.print(f"📝 Your answer: {answer}")

            eval_data = self.evaluate_answer(q, answer)
            rec = QARecord(
                question=q,
                answer=answer,
                feedback=eval_data.get("feedback", ""),
                score=int(eval_data.get("score", 3))
            )
            self.records.append(rec)
            console.print(Panel.fit(Markdown(f"**Feedback**\n\n{rec.feedback}"), title=f"Score: {rec.score}/5"))

        self.summary()

    def evaluate_answer(self, question, answer):
        messages = [
            {"role": "system", "content": f"You are an experienced interviewer for {self.cfg.topic}."},
            {"role": "user", "content": json.dumps({
                "question": question,
                "candidate_answer": answer,
                "seniority": self.cfg.level
            })},
        ]
        resp = self.client.chat.completions.create(
            model=self.cfg.model,
            messages=messages,
            temperature=0.3,
            response_format={"type": "json_object"},
        )
        try:
            return json.loads(resp.choices[0].message.content)
        except Exception:
            return {"feedback": "Parsing error.", "score": 3}

    def summary(self):
        table = Table(title="Session Summary")
        table.add_column("#")
        table.add_column("Question")
        table.add_column("Score")
        for i, r in enumerate(self.records, 1):
            table.add_row(str(i), r.question, str(r.score))
        avg = sum(r.score for r in self.records) / len(self.records)
        console.print(table)
        console.print(f"Average Score: {avg:.2f}")

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--topic", choices=SUPPORTED_TOPICS.keys(), default="qa")
    p.add_argument("--level", choices=["junior", "mid", "senior"], default="mid")
    p.add_argument("--rounds", type=int, default=2)
    p.add_argument("--model", default="gpt-4.1-mini")
    args = p.parse_args()
    return SessionConfig(topic=args.topic, level=args.level, rounds=args.rounds, model=args.model)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        console.print("OPENAI_API_KEY not set")
        sys.exit(1)
    cfg = parse_args()
    InterviewAgent(cfg).run()