import pollinations
import time

def generateImages(prompts):
    for i, prompt in enumerate(prompts, start=1):  # Start counting from 1
        image = None
        for attempt in range(3):  # Try up to 3 times
            try:
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
                    prompt="A pixel-art, minimalist, black-and-white, line drawing, stick man, simple, clean, no shading, white background, thin lines, round head " + prompt + " art style is retro, pixelated, and reminiscent of 8-bit or 16-bit video game graphics, with clean lines and blocky/pixelated, plain background"
                )
                break  # If generation succeeds, exit the retry loop
            except Exception as e:
                print(f"Attempt {attempt+1} failed to generate image for prompt '{prompt}': {e}")
                if attempt < 2:  # If not the last attempt, wait before retrying
                    time.sleep(5)
                else:
                    print(f"Failed to generate image for prompt '{prompt}' after 3 attempts.")
        
        # If image was successfully generated, try to save it
        if image is not None:
            try:
                print(image.prompt, image.response)
                image.save(file=f"./raw/images/{i}.png")
            except Exception as e:
                print(f"Failed to save image for prompt '{prompt}': {e}")