# from mutagen.mp3 import MP3

# # Store the audio file path
# audio_path = r"E:\programs\Youtube_shorts\input\audio.mp3"

# try:
#     # Try to open the MP3 file
#     audio = MP3(audio_path)

#     # Check the audio duration
#     print("Audio file is valid!")
#     print("Duration:", round(audio.info.length, 2), "seconds")

# except Exception as e:
#     # Show an error if the file is not a valid MP3
#     print("Audio file is invalid!")
#     print("Error:", e)


from moviepy import AudioFileClip

audio_path = r"E:\programs\Youtube_shorts\input\audio.mp3"

print("Loading audio...")

audio = AudioFileClip(audio_path)

print("Audio loaded successfully!")
print("Duration:", audio.duration)

audio.close()