from moviepy import ImageClip, AudioFileClip

# --------------------------------------------------
# FILE LOCATIONS
# --------------------------------------------------

image_path = r"E:\programs\Youtube_shorts\input\image.png"
audio_path = r"E:\programs\Youtube_shorts\input\audio.mp3"
output_path = r"E:\programs\Youtube_shorts\output\my_short.mp4"


# --------------------------------------------------
# LOAD IMAGE
# --------------------------------------------------

image = ImageClip(image_path)
# print("Image loaded successfully!")


# --------------------------------------------------
# LOAD AUDIO
# --------------------------------------------------

audio = AudioFileClip(audio_path)
# print("Audio loaded successfully!")

# --------------------------------------------------
# SET VIDEO SIZE
# 9:16 vertical format
# --------------------------------------------------

video_width = 1080
video_height = 1920

image = image.resized(height=video_height)

# Crop image to 9:16
image = image.cropped(
    width=video_width,
    height=video_height,
    x_center=image.w / 2,
    y_center=image.h / 2
)


# --------------------------------------------------
# SET VIDEO DURATION
# Same duration as audio
# --------------------------------------------------

image = image.with_duration(audio.duration)


# --------------------------------------------------
# ADD AUDIO
# --------------------------------------------------

video = image.with_audio(audio)


# --------------------------------------------------
# EXPORT VIDEO
# --------------------------------------------------

video.write_videofile(
    output_path,
    fps=30,
    codec="libx264",
    audio_codec="aac"
)


print("YouTube Short created!")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# # ============================================================
# # IMPORT REQUIRED TOOLS FROM MOVIEPY
# # ============================================================

# # ImageClip:
# #   Used to load an image and treat it like a video clip.
# #
# # AudioFileClip:
# #   Used to load an audio file such as MP3.
# #
# # We need both because our final video will contain:
# #       IMAGE + AUDIO
# #
# from moviepy import ImageClip, AudioFileClip


# # ============================================================
# # FILE LOCATIONS
# # ============================================================

# # Location of the input image.
# #
# # The "r" before the path means "raw string".
# # It tells Python to treat "\" as a normal character.
# #
# # Example:
# # E:\programs\Youtube_shorts\input\image.png
# #
# image_path = r"E:\programs\Youtube_shorts\input\image.png"


# # Location of the input audio file.
# #
# # This audio will become the sound/voice of our video.
# #
# audio_path = r"E:\programs\Youtube_shorts\input\audio.mp3"


# # Location where the final video will be saved.
# #
# # Our program will create:
# #
# #     my_short.mp4
# #
# # inside the "output" folder.
# #
# output_path = r"E:\programs\Youtube_shorts\output\my_short.mp4"


# # ============================================================
# # LOAD IMAGE
# # ============================================================

# # Load the image using MoviePy.
# #
# # ImageClip converts our image file into a MoviePy object
# # that we can use as part of a video.
# #
# # Before:
# #
# #     image.png
# #
# # After:
# #
# #     image = ImageClip object
# #
# image = ImageClip(image_path)


# # If you want to check whether the image was loaded,
# # you can uncomment the following line:
# #
# # print("Image loaded successfully!")


# # ============================================================
# # LOAD AUDIO
# # ============================================================

# # Load the MP3 audio file.
# #
# # AudioFileClip reads the audio and gives us an object
# # that MoviePy can use in the video.
# #
# # The audio object also contains useful information such as:
# #
# #     audio.duration
# #
# # which tells us how many seconds the audio lasts.
# #
# audio = AudioFileClip(audio_path)


# # If you want to check whether the audio was loaded,
# # you can uncomment the following line:
# #
# # print("Audio loaded successfully!")


# # ============================================================
# # SET VIDEO SIZE
# # ============================================================

# # We want to create a vertical YouTube Short.
# #
# # Video dimensions:
# #
# #     Width  = 1080 pixels
# #     Height = 1920 pixels
# #
# # This gives us a 9:16 vertical video.
# #
# #       1080
# #    ┌─────────┐
# #    │         │
# #    │         │
# #    │         │
# #    │  VIDEO  │  1920
# #    │         │
# #    │         │
# #    │         │
# #    └─────────┘
# #
# # 1080 : 1920
# #     ↓
# #     9 : 16
# #
# video_width = 1080
# video_height = 1920


# # ============================================================
# # RESIZE THE IMAGE
# # ============================================================

# # Resize the image so that its height becomes 1920 pixels.
# #
# # Why?
# #
# # Our final video height is 1920 pixels.
# # We first make the image tall enough and then crop it
# # to the required 1080 × 1920 size.
# #
# # Example:
# #
# # Original image:
# #
# #     1920 × 1080
# #
# # After resizing:
# #
# #     height = 1920
# #
# image = image.resized(height=video_height)


# # ============================================================
# # CROP IMAGE TO 9:16
# # ============================================================

# # After resizing, the image may still be wider than
# # our required video width.
# #
# # Therefore, we crop the image.
# #
# # Final required size:
# #
# #     Width  = 1080
# #     Height = 1920
# #
# image = image.cropped(
    
#     # Width of the cropped area.
#     # 1080 pixels.
#     width=video_width,

#     # Height of the cropped area.
#     # 1920 pixels.
#     height=video_height,

#     # Crop around the horizontal center of the image.
#     #
#     # image.w = current image width
#     # image.w / 2 = center of the image horizontally
#     #
#     x_center=image.w / 2,

#     # Crop around the vertical center of the image.
#     #
#     # image.h = current image height
#     # image.h / 2 = center of the image vertically
#     #
#     y_center=image.h / 2
# )


# # ============================================================
# # SET IMAGE DURATION
# # ============================================================

# # An image itself does not have a duration.
# #
# # For example:
# #
# #     image.png
# #
# # is simply a picture.
# #
# # But a video needs to know:
# #
# #     "How long should this picture be displayed?"
# #
# # We use the audio duration for this.
# #
# # Example:
# #
# #     audio.duration = 7 seconds
# #
# # Then:
# #
# #     image duration = 7 seconds
# #
# # This means the image stays on screen for exactly
# # the same amount of time as the audio.
# #
# image = image.with_duration(audio.duration)


# # ============================================================
# # ADD AUDIO TO THE IMAGE
# # ============================================================

# # Now we combine:
# #
# #     IMAGE
# #       +
# #     AUDIO
# #
# # into one video object.
# #
# # Before:
# #
# #     image = image clip
# #     audio = audio clip
# #
# # After:
# #
# #     video = image + audio
# #
# video = image.with_audio(audio)


# # ============================================================
# # EXPORT / CREATE THE FINAL VIDEO
# # ============================================================

# # Up to this point, the video exists as a MoviePy object
# # in Python's memory.
# #
# # write_videofile() actually creates the MP4 file
# # on your computer.
# #
# video.write_videofile(

#     # Where should the video be saved?
#     #
#     # E:\programs\Youtube_shorts\output\my_short.mp4
#     #
#     output_path,

#     # FPS = Frames Per Second
#     #
#     # 30 means the video contains approximately
#     # 30 frames every second.
#     #
#     # Example:
#     #
#     # 10-second video × 30 FPS
#     # = approximately 300 frames
#     #
#     fps=30,

#     # Video codec.
#     #
#     # libx264 is an implementation of the H.264
#     # video compression standard.
#     #
#     # It is commonly used for MP4 videos.
#     #
#     codec="libx264",

#     # Audio codec.
#     #
#     # AAC is used to encode the audio portion
#     # of our MP4 video.
#     #
#     audio_codec="aac"
# )


# # ============================================================
# # DISPLAY A MESSAGE AFTER VIDEO CREATION
# # ============================================================

# # This simply prints a message in PowerShell/Command Prompt
# # after MoviePy finishes creating the video.
# #
# # It does NOT create the video.
# # write_videofile() above is what creates the video.
# #
# print("YouTube Short created!")
