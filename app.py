import whisper

from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# Step 1: Transcribe audio with Whisper
def transcribe_audio(audio_file):
    model = whisper.load_model("base")  # Use "base" model for simplicity
    result = model.transcribe(audio_file, word_timestamps=True)  # Get word-level timestamps
    return result["segments"]

# Step 2: Create two-word SRT content
def create_srt_from_words(segments):
    srt_content = ""
    index = 1
    words = []
    
    # Collect all words with timestamps from segments
    for segment in segments:
        words.extend(segment["words"])
    
    # Pair words into two-word chunks
    for i in range(0, len(words) - 1, 2):  # Step by 2 to pair words
        word1 = words[i]
        word2 = words[i + 1] if i + 1 < len(words) else {"word": "", "start": word1["end"], "end": word1["end"]}
        
        start_time = word1["start"]
        end_time = word2["end"]
        
        # Convert times to SRT format (e.g., 00:00:01,000)
        start_srt = f"{int(start_time // 3600):02d}:{int((start_time % 3600) // 60):02d}:{int(start_time % 60):02d},{int((start_time % 1) * 1000):03d}"
        end_srt = f"{int(end_time // 3600):02d}:{int((end_time % 3600) // 60):02d}:{int(end_time % 60):02d},{int((end_time % 1) * 1000):03d}"
        
        # Add to SRT content
        srt_content += f"{index}\n{start_srt} --> {end_srt}\n{word1['word']} {word2['word']}\n\n"
        index += 1
    
    # Save SRT file
    with open("subtitles.srt", "w") as f:
        f.write(srt_content)
    return "subtitles.srt"

# Step 3: Main video creation
# List of image files
images = ["1.jpg", "2.jpg"]

# Load the audio
audio = AudioFileClip("audio.mp3")

# Calculate duration per image (evenly split audio duration)
duration_per_image = audio.duration / len(images)

# Create a list of image clips with assigned durations
clips = [ImageClip(img).set_duration(duration_per_image) for img in images]

# Concatenate the image clips into one video
video = concatenate_videoclips(clips, method="compose")


# Add the audio
video = video.set_audio(audio)

# Step 4: Transcribe and generate SRT
segments = transcribe_audio("audio.mp3")
srt_file = create_srt_from_words(segments)

# Step 5: Add subtitles to the video
# Note: MoviePy doesn't directly support SRT, so we create TextClips manually
subtitle_clips = []
with open(srt_file, "r") as f:
    lines = f.read().splitlines()
    i = 0
    while i < len(lines):
        if lines[i].isdigit():  # SRT entry number
            time_line = lines[i + 1].split(" --> ")
            start_time = sum(x * float(t) for x, t in zip([3600, 60, 1, 0.001], time_line[0].replace(',', '.').split(':')))
            end_time = sum(x * float(t) for x, t in zip([3600, 60, 1, 0.001], time_line[1].replace(',', '.').split(':')))
            text = lines[i + 2]
            
            # Create a TextClip for this subtitle
            txt_clip = (TextClip(text, fontsize=40, color='white', bg_color='black')
                        .set_position(('center', 'bottom'))
                        .set_start(start_time)
                        .set_end(end_time))
            
            subtitle_clips.append(txt_clip)
            i += 4  # Skip to next SRT block
        else:
            i += 1

# Combine video with subtitles
final_video = CompositeVideoClip([video] + subtitle_clips)

# Save the result
final_video.write_videofile("output_video.mp4", fps=24, codec="libx264")