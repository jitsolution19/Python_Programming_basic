from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Step 1: Hindi Text
hindi_text = "या देवी सर्वभूतेषु शक्ति-रूपेण संस्थिता। नमस्तस्यै नमस्तस्यै नमस्तस्यै नमो नमः॥"

# Step 2: Convert to Speech (Hindi)
tts = gTTS(text=hindi_text, lang='hi')
tts.save("voice.mp3")

# Step 3: Load Voice and Background Music
voice = AudioSegment.from_file("voice.mp3", format="mp3")
music = AudioSegment.from_file("background.mp3", format="mp3")  # provide your background track

# Step 4: Adjust volume levels
voice = voice + 5            # increase voice volume
music = music - 10           # reduce music volume

# Step 5: Mix both (overlay)
combined = music.overlay(voice, position=2000)  # start voice after 2 sec

# Step 6: Export Final Music
combined.export("hindi_music.mp3", format="mp3")

# Step 7: Play it
play(combined)
