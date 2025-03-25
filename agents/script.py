from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from others.loading_animation import loadingAnimation
import json

def generate_script(title):
    
    sys_instruct = """
    You are video content script writer, generate script follow this structure: hooks -> body -> conclusion. 

    Respond strictly RULES:
    avoids any video-style formatting, like scene descriptions, structure or visual instructions, markdown formatting. Use simple english and easy words

    Example: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    
    
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction=sys_instruct),
        contents=[f"Create me a script base on this topic: {title}"]
    )

    loadingAnimation("Generating a script")
    llm_response = response.text
    print(llm_response)
    return llm_response

