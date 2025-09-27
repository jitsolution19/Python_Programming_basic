'''
Created on 29-Aug-2025

@author: jeete
'''
import whisper
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load Whisper model (base = fast, medium/large = more accurate)
model = whisper.load_model("base")

# Example: transcribe audio file (user�s speech)
result = model.transcribe("voice_input.wav")
command = result["text"].lower()
print("Recognized Voice Command:", command)

# Selenium browser automation
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Example: If user says "search selenium webdriver"
if "search" in command:
    search_text = command.replace("search", "").strip()
    box = driver.find_element(By.NAME, "q")
    box.send_keys(search_text)
    box.submit()

time.sleep(5)
driver.quit()