'''
Created on 29-Aug-2025

@author: jeete
'''
import sounddevice as sd
from scipy.io.wavfile import write

# Recording settings
fs = 16000  # Sample rate
seconds = 5  # Duration of recording

print("🎙️ Recording... Speak now!")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()  # Wait until recording is finished
write("voice_input.wav", fs, recording)  # Save as WAV file
print("✅ Saved as voice_input.wav")