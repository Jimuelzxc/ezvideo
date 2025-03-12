
# Create Title
from agents.title import generateTitle
selected_title = generateTitle()

# Create Script
from agents.script import generateScript
text = generateScript(selected_title)

# Script to audio
from agents.speech import generateAudio
audio= generateAudio(text, selected_title)
audio_path = audio["path"]
audio_duration = audio["duration"]


# Script to image prompts
from agents.image_prompt import generateImagePrompts
image_prompts = generateImagePrompts(audio_duration, text)
print("IMAGE PROMPTS: ", image_prompts)

#Image prompts to Images
from agents.image_generator import generateImages
generateImages(image_prompts)

# Editor
from editor import generateVideo
final_output = generateVideo(audio_path, selected_title)






