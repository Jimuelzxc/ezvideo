import requests
import json
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types


load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")


def openrouter(system, text):
  response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
      "Authorization": f"Bearer {openrouter_api_key}",
      "Content-Type": "application/json",
    },
    data=json.dumps({
      "model": "deepseek/deepseek-r1:free",
      "messages": [
          {
              "role": "system",
              "content":system
          },
        {
          "role": "user",
          "content": text
        }
      ],
    })
  )
  response_data = response.json()
  text = response_data['choices'][0]['message']['content']
  return text

  
def gemini(system, text):
  client = genai.Client(api_key=gemini_api_key)
  response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=system),
    contents=[text]
    )
  return response.text
  