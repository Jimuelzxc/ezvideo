from dotenv import load_dotenv
import os
from others.loading_animation import loadingAnimation
from others.models import *
import json



sys_instruct = """You are a YouTube content strategist specializing in maximizing viewer engagement and retention through effective video titles. Your goal is to create attention-grabbing YouTube video titles. Use the following to inform your guide:  

**Task:**  
Write a comprehensive guide for YouTube creators that includes:  
- A step-by-step breakdown of how to create clickbaity yet honest titles.
- Keep titles under 60-70 characters for readability and ensure they are descriptive and search-optimized.  
- When making titles, always emphasize “You” or how to:
    - Example:
        - Instead of: 3 Communication mistakes to avoid
        - Do this: 3 communication mistakes you need to avoid.

Notes:
- Use simple English and easy words.

Respond strictly in array, no JSON wrapper. following structure:
[
    "titles",
    "titles2",
    "etc..."
]
"""

def generate_title_client():
    # System instructions for the AI (unchanged)
    print("What topic are you interested in?")
    topic = input("")
    while True:
        # Get titles from AI
        text = f"Generate me 10 titles for content about {topic}"
        response = openrouter(sys_instruct, text)
        print(response)
        titles = json.loads(response)

        # Show titles
        for i, title in enumerate(titles, 1):
            print(f"[{i}] {title}")

        # Get user's choice
        choice = input("\nPick a number (1-10) or 11 to retry: ")
        try:
            choice = int(choice)
            if choice == 11:
                print("Getting new titles...")
                continue
            if 1 <= choice <= 10:
                selected_title = titles[choice - 1]
                print(f"You chose: {selected_title}")
                break
            print("Choose 1-11 only")
        except ValueError:
            print("Enter a number")

    return selected_title         

def generate_titles_api(topic):
    # System instructions for the AI (unchanged)
    text = f"Generate me 10 titles for content about {topic}"
    response = openrouter(sys_instruct, text)
    print(response)
    titles = json.loads(response)
    return titles