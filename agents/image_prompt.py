import json
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from others.loading_animation import loadingAnimation


def generateImagePrompts(duration, text): 
    contents = f"""
    Create list of prompts (the duration is {duration}  it depends how long the script/video timing it if you want, and second person focus on "you" means always show a person as much as possible) for image generation base on the scripts i provide. and put in array (Make the images easy to understand and literal, avoiding abstract or overly complex visuals. focusing on the subject, body language, and expression, with minimal objects (like a wall or book). Avoid abstract or overly complex visuals—simplicity is key—and do not include text on the images) NOTES: MAKE SURE THE PROMPT IT FITS LINE BY LINE ON THE SCRIPT and read the script properly make sure, the image compliment to the script. make first prompt consistent for hooks

    Respond strictly in array format, without any JSON wrapper or code block formatting. Your response should follow this exact structure:
    [
        "prompt",
        "prompt2",
        "etc..."
    ]

    Script: 
    {text}

    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=contents
            )
            llm_response = response.text
            print(llm_response)
            image_prompts = json.loads(llm_response)  # Directly a list
            return image_prompts
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(5)  # Wait 5 seconds before retrying
            else:
                raise Exception("Failed to generate image prompts after 3 attempts.")