"""

def create_srt_from_words(segments, words_per_subtitle, srt_filename):
    # Ensure the directory exists before writing the file
    os.makedirs(os.path.dirname(srt_filename), exist_ok=True)
    
    srt_content = ""
    index = 1
    words = []

    # Collect all words from segments
    for segment in segments:
        words.extend(segment["words"])

    # Loop through words in steps of words_per_subtitle
    for i in range(0, len(words), words_per_subtitle):
        # Get the group of words (up to words_per_subtitle)
        group = words[i:i + words_per_subtitle]
        
        # Start time is from the first word, end time from the last word
        start_time = group[0]["start"]
        end_time = group[-1]["end"]
        
        # Join all words in the group with spaces, removing commas and periods
        subtitle_text = " ".join(word["word"].replace(",", "").replace(".", "") for word in group)

        # Format timestamps for SRT
        start_srt = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d},{int((start_time % 1) * 1000):03d}"
        end_srt = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d},{int((end_time % 1) * 1000):03d}"

        # Add subtitle entry to SRT content
        srt_content += f"{index}\n{start_srt} --> {end_srt}\n{subtitle_text.strip()}\n\n"
        index += 1

    # Write to SRT file
    with open(srt_filename, "w", encoding="utf-8") as f:
        f.write(srt_content)
    return srt_filename   
    


"""

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
    print(result["segments"])

    
# Step 2: Create SRT from segments without splitting into fixed word counts
def create_srt_from_segments(segments, srt_filename):
    # Ensure the directory exists before writing the file
    os.makedirs(os.path.dirname(srt_filename), exist_ok=True)
    
    srt_content = ""
    
    for index, segment in enumerate(segments, start=1):
        start_time = segment["start"]
        end_time = segment["end"]
        # Use the complete text of the segment
        text = segment["text"].strip()
        
        # Format timestamps for SRT (HH:MM:SS,mmm)
        start_srt = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d},{int((start_time % 1) * 1000):03d}"
        end_srt = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d},{int((end_time % 1) * 1000):03d}"
        
        # Add subtitle entry to SRT content
        srt_content += f"{index}\n{start_srt} --> {end_srt}\n{text}\n\n"
    
    # Write to SRT file
    with open(srt_filename, "w", encoding="utf-8") as f:
        f.write(srt_content)
    return srt_filename



   

def create_video_with_images_and_audio(images, audio_file, output_file):
    audio = AudioFileClip(audio_file)
    duration_per_image = audio.duration / len(images)
    
    # Create image clips with initial durations
    clips = [ImageClip(img).set_duration(duration_per_image) for img in images]
    
    # Concatenate clips to form the initial video
    video = concatenate_videoclips(clips, method="compose")
    
    # Ensure video duration matches or exceeds audio duration
    if video.duration < audio.duration:
        extra_duration = audio.duration - video.duration
        # Extend the last clip's duration
        clips[-1] = clips[-1].set_duration(clips[-1].duration + extra_duration)
        # Re-concatenate with the adjusted clip
        video = concatenate_videoclips(clips, method="compose")
    
    # Attach the audio to the video
    video = video.set_audio(audio)
    
    # Export the final video
    video.write_videofile(output_file, fps=24, codec="libx264")
    return output_file

# Step 4: Burn Subtitles using FFmpeg
def burn_subtitles_ffmpeg(input_video, srt_file, output_file):
    cmd = [


        "ffmpeg",
            "-i", input_video,
            "-vf", f"subtitles={srt_file}:force_style='Fontsize=10'",  # Adjust the font size as needed
            "-c:a", "copy",
            output_file
    ]
    
    subprocess.run(cmd, check=True)
    return output_file

import re
def generateVideo(audioPath, title):
    title = title.lower()
    title = title.replace(" ", "_")
    title = re.sub(r'[^\w-]', '', title)     
    
    subtitle_path = f"./raw/subtitles/{title}.srt"  
    video_path = f"./raw/videos/temp_video_{title}.mp4"
    final_video_path = f"./final/{title}.mp4"  

    images = [str(p) for p in sorted(Path('./raw/images').glob('*.png'), key=lambda p: int(p.stem))]
    segments = transcribe_audio(audioPath)
    srt_file = create_srt_from_segments(segments, subtitle_path)
    video_file = create_video_with_images_and_audio(images, audioPath, video_path)
    final_output = burn_subtitles_ffmpeg(video_file, srt_file, final_video_path)
    return final_output