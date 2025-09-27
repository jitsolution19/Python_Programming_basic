'''
Created on 29-Aug-2025

@author: jeete
'''
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import shutil
import sys

# Step 0: Check FFmpeg availability
def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("❌ FFmpeg not found!")
        print("👉 Please install FFmpeg and add it to PATH:")
        print("   1. Download: https://ffmpeg.org/download.html")
        print("   2. Extract and add 'bin' folder to PATH")
        print("   3. Restart your terminal/IDE")
        sys.exit(1)
    else:
        print("✅ FFmpeg found.")

# Step 1: Record voice
def record_voice(filename="voice_input.wav", duration=10, fs=16000):
    print("🎙️ Recording... Speak your command now")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Voice saved as {filename}")
    return filename

# Step 2: Transcribe with Whisper
def transcribe_audio(filename):
    model = whisper.load_model("base").to("cpu")
    result = model.transcribe(filename)
    text = result["text"].lower().strip()
    print("📝 Transcribed Command:", text)
    return text

# Step 3: Run Selenium action based on voice command
def run_selenium(command):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    
    if "search" in command:
        search_text = command.replace("search", "").strip()
        box = driver.find_element(By.NAME, "q")
        box.send_keys(search_text)
        box.submit()
        print(f"🔍 Searching for: {search_text}")
    
    time.sleep(5)
    driver.quit()

# === MAIN FLOW ===
check_ffmpeg()                      # Check before doing anything
filename = record_voice()            # Record audio
command = transcribe_audio(filename) # Convert speech → text
print("Instruction fetch"+command)
# run_selenium(command)                # Run action