# Using the pollinations pypi package

## pip install pollinations

import pollinations
prompts2 = [
  "A person looking confused and disoriented, with question marks swirling around their head, while a shadowy figure whispers in their ear.",
  "A hand holding a match trying to light a gas lamp, with the gas lamp labeled 'Your Reality' and the match labeled 'Doubt'.",
  "Two people talking. One person is calm and holding a notebook with notes, while the other person is gesturing dismissively and saying, 'That never happened.'",
  "A person standing firm, with a thought bubble above their head showing a clear memory, while another person tries to erase the thought bubble with a distorted eraser.",
  "A person inside a clear bubble, representing their reality, while toxic green gas labeled 'Gaslighting' seeps in from outside.",
  "A split image: One side shows a clear, organized journal entry, the other side shows a distorted, blurry version of the same event."
]
promptsTwo = ["line art, stick man, minimalist. sit, on the table, on his computer"]


promptsThree = [
    "A person sitting at a desk, trying to study but getting distracted by their phone, showing TikTok on the screen.",
    "A classroom setting where a student looks bored and overwhelmed, surrounded by textbooks and notes, emphasizing the struggle of traditional learning methods.",
    "A person studying math, not just memorizing formulas but analyzing and understanding why they work, with thought bubbles showing deeper understanding.",
    "Someone practicing a new language in a real conversation, perhaps speaking with a friend or using a language app, looking slightly awkward but determined.",
    "A person quizzing themselves by closing a book, looking away from a screen, and trying to recall what they’ve learned, with a mix of confidence and uncertainty.",
    "A gym setting but for the brain—showing a person 'working out' their mind with flashcards or mental exercises, representing active recall.",
    "A plant being watered slowly over time, comparing it to spaced repetition in learning, with a thriving, healthy plant symbolizing a well-developed memory.",
    "A person teaching what they’ve learned to a friend, sibling, or even a pet, demonstrating the 'learning by teaching' method, with simple explanations and engagement.",
    "Someone taking a break from studying, relaxing with a walk, a snack, or just enjoying a few minutes of rest, avoiding burnout.",
    "A person experimenting with different study tools—books, videos, apps—surrounded by various learning materials, showing curiosity and adaptability.",
    "A person being patient with themselves, looking at a calendar or a progress chart, showing that learning is a gradual process, not a race."
]


promptsSTICKMAN = [ # STICKMAN PROMPT
  "You sitting on a couch, looking stressed with a notebook in hand.",
  "You standing in front of a huge wall, looking overwhelmed.",
  "You smiling while doing push-ups on the floor.",
  "You sitting at a desk, looking happy with a notebook.",
  "You walking forward on a path, looking confident.",
  "You standing in front of a mirror, smiling proudly."
]

prompts = [
  "A close-up of you, a person with wide eyes and a stiff, awkward frown, standing alone against a plain wall, arms crossed tightly like you’re frozen in a crowd.",
  "A long shot of you, head down and shoulders slumped, looking nervous in a busy line of people blurred in the background, clutching a coffee cup.",
  "A medium shot of you, eyebrows raised with a hopeful nod, standing against a plain wall, hands in pockets like you’re realizing something simple.",
  "A close-up of you smiling warmly, eyes bright and head tilted slightly, against a soft-colored wall, radiating friendliness with relaxed shoulders.",
  "A long shot of you chatting with another person, pointing casually at the sky with a curious expression, standing outside with just a cloudy sky behind you.",
  "A medium shot of you, arms relaxed and a genuine grin on your face, leaning slightly toward someone blurred beside you, a book on a table nearby.",
  "A long shot of you in a grocery line, smiling at a stranger while holding a basket, head tilted like you’re asking a question, with shelves faintly visible.",
  "A close-up of you, eyes wide with surprise and a small, natural smile, hands open as if amazed, against a plain wall.",
  "A medium shot of you looking directly forward, confident and inviting, one hand gesturing outward, a single chair in the background like you’re calling someone to join."
]


for i, prompt in enumerate(prompts, start=1):  # Start counting from 1
    image_model = pollinations.Image(
        model=pollinations.Image.flux(),
        seed="random",
        width=1920,
        height=1080,
        enhance=False,
        nologo=True,
        private=True,
        safe=False,
        referrer="pollinations.py"
    )

    image = image_model(
        prompt="A pixel-art, minimalist, black-and-white, line drawing, stick man, simple, clean, no shading, white background, consistent style, thin lines, round head"+ prompt+"art style is retro, pixelated, and reminiscent of 8-bit or 16-bit video game graphics, with clean lines and blocky/pixelated, [[[minimalist]]], plain background"
#PENCIL        prompt= "A simple drawing of" + prompt + "on white paper, in the style of pencil drawing, minimalistic"
#STICKMAN        prompt=prompt + " [[black and white]], [[[[NO TEXT]]]], [[[[stickman]]]], [[[[line art]]]], [[minimalist]]"
#        prompt=prompt+"drawing in the style of the new contemporary artist,using black ink on white paper. The background wall has purple grid lines. The surreal style also calls to mind traditional illustration with comic drawing a cartoon-like quality "


    )

    print(image.prompt, image.response)

    # Save with numbered filename (e.g., "1.png", "2.png", etc.)
    image.save(
        file=f"./images/{i}.png"
    )