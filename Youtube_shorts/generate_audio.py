from gtts import gTTS

# Write the text you want to convert into speech
text_to_speak = "A Python list is used to store multiple values in a single variable."

# Convert the text into speech
tts = gTTS(text=text_to_speak, lang="en")

# Save the speech as an MP3 file
tts.save(r"E:\programs\Youtube_shorts\input\audio.mp3")

# Display a success message
print("MP3 file created successfully!")