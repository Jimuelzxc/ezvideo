
import pollinations 
 
image_model = pollinations.Image(
    model=pollinations.Image.flux(),
    seed="random",
    width=1080,
    height=1920,
    enhance=False,
    nologo=True,
    private=True,
    safe=False,
    referrer="pollinations.py"
)

image = image_model(
    prompt="A pixel-art, minimalist, black-and-white, line drawing, stick man, simple, clean, no shading, white background, consistent style, thin lines, round head art style is retro, pixelated, and reminiscent of 8-bit or 16-bit video game graphics, with clean lines and blocky/pixelated, [[[minimalist]]], plain background"
#PENCIL        prompt= "A simple drawing of" + prompt + "on white paper, in the style of pencil drawing, minimalistic"
#STICKMAN        prompt=prompt + " [[black and white]], [[[[NO TEXT]]]], [[[[stickman]]]], [[[[line art]]]], [[minimalist]]"
#        prompt=prompt+"drawing in the style of the new contemporary artist,using black ink on white paper. The background wall has purple grid lines. The surreal style also calls to mind traditional illustration with comic drawing a cartoon-like quality "


)

print(image.prompt, image.response)
image.save(
    file=f"test.png"
)