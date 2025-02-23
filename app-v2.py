import whisper

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})
import subprocess
import os
import shutil
from pathlib import Path
# Step 1: Transcribe audio with Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, word_timestamps=True)
    return result["segments"]

# Step 2: Create SRT file
def create_srt_from_words(segments, srt_filename="subtitles.srt"):
    srt_content = ""
    index = 1
    words = []

    for segment in segments:
        words.extend(segment["words"])

    for i in range(0, len(words), 2):
        word1 = words[i]
        word2 = words[i + 1] if i + 1 < len(words) else None

        start_time = word1["start"]
        end_time = word2["end"] if word2 else word1["end"]

        start_srt = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d},{int((start_time % 1) * 1000):03d}"
        end_srt = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d},{int((end_time % 1) * 1000):03d}"

        # Avoid extra space by only adding a space if word2 exists
        subtitle_text = word1["word"] + (f" {word2['word']}" if word2 else "")

        srt_content += f"{index}\n{start_srt} --> {end_srt}\n{subtitle_text.strip()}\n\n"
        index += 1

    with open(srt_filename, "w", encoding="utf-8") as f:
        f.write(srt_content)
    return srt_filename

    


# Step 3: Create Video with MoviePy
def create_video_with_images_and_audio(images, audio_file, output_file="temp_video.mp4"):
    audio = AudioFileClip(audio_file)
    duration_per_image = audio.duration / len(images)


    
    clips = [ImageClip(img).set_duration(duration_per_image) for img in images]
    video = concatenate_videoclips(clips, method="compose").set_audio(audio)
    
    video.write_videofile(output_file, fps=24, codec="libx264")
    return output_file

# Step 4: Burn Subtitles using FFmpeg
def burn_subtitles_ffmpeg(input_video, srt_file, output_file="output_video_with_subtitles.mp4"):
    cmd = [


        "ffmpeg",
            "-i", input_video,
            "-vf", f"subtitles={srt_file}:force_style='Fontsize=10'",  # Adjust the font size as needed
            "-c:a", "copy",
            output_file
    ]
    
    subprocess.run(cmd, check=True)
    return output_file

# Execute the pipeline
#images = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]

#folder_path = "./images"

# Get the list of files in the folder
#files = os.listdir(folder_path)

# Filter out only the PNG files
#png_files = [f for f in files if f.endswith('.png')]
#images = [f"./images/{i}.png" for i in range(1, 11)]
images = [str(p) for p in sorted(Path('./images').glob('*.png'), key=lambda p: int(p.stem))]
# images = [file for file in os.listdir("./images") if file.endswith('.png')]
segments = transcribe_audio("./audios/The Easy Way to Talk to Anyone, Anywhere.mp3")
srt_file = create_srt_from_words(segments)
video_file = create_video_with_images_and_audio(images, "./audios/The Easy Way to Talk to Anyone, Anywhere.mp3")
final_output = burn_subtitles_ffmpeg(video_file, srt_file)

# Path to the images folder
#folder_path = './images'
# Delete everything in the folder
#shutil.rmtree(folder_path)
# Recreate the folder (optional)
#os.makedirs(folder_path)
print(f"Video with subtitles saved as: {final_output}")