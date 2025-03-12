from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from others.loading_animation import loadingAnimation
import json



def generateTitle():
    # Get the topic once, outside the loop
    print("What topic are you interested in? ")
    topic = input("")

    # System instructions for the AI (unchanged)
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

    # Initialize the AI client (unchanged)
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key is None:
        raise ValueError("API_KEY is not set in the environment")

    client = genai.Client(api_key=api_key)
    # Loop to generate and select titles
    while True:
        # Generate titles
        print("Generating titles for your topic...")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=sys_instruct),
            contents=[f"Generate me 10 titles for content about {topic}"]
        )
        llm_response = response.text
        # Removed print(llm_response) assuming it was for debugging
        titles = json.loads(llm_response)  # Convert response to a list

        # Display the titles with loading animation
        loadingAnimation("Generating Titles")
        for i, title in enumerate(titles, 1):
            print(f"[{i}] {title}")

        # Prompt for user input with regeneration option
        print("\nEnter the number of the title you want to select (1-10), or 11 to regenerate:")
        try:
            choice = int(input())
            if choice == 11:
                print("Regenerating titles...")
                continue  # Go back to the start of the loop to regenerate
            elif 1 <= choice <= 10:
                selected_title = titles[choice - 1]
                print(f"\nYou selected: {selected_title}")
                break  # Exit the loop with the selected title
            else:
                print("Please enter a number between 1 and 11.")
        except ValueError:
            print("Please enter a valid number.")

    # Return the selected title
    return selected_title