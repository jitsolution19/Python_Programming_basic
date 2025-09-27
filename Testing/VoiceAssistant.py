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
import os
# Step 1: Record voice
def record_voice(filename="voice_input.wav", duration=10, fs=16000):
    print("🎙️ Recording... Speak your command now")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Voice saved as {filename}")
    return filename

# Step 2: Transcribe with Whisper (force CPU to avoid FP16 warnings)
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
filename = record_voice()            # Record 5 sec audio
# filename = "voice_input.wav"
# filepath = os.path.abspath(filename)
command = transcribe_audio(filename) # Convert speech → text
run_selenium(command)                # Execute in browser



# filename = "voice_input.wav"
# filepath = os.path.abspath(filename)
# print("📂 File saved at:", filepath)