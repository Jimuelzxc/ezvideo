import pollinations
import time
import os
import random
"""
def generateImages(prompts):
    main_seed = 3174564238  # Default seed

    for i, prompt in enumerate(prompts, start=1):  # Start counting from 1
        image = None
        satisfied = False
        current_seed = main_seed  # Start with the main seed

        while not satisfied:
            # Try generating the image up to 3 times with the current seed
            for attempt in range(3):
                try:
                    image_model = pollinations.Image(
                        model=pollinations.Image.flux(),
                        seed=current_seed,  # Use the current seed (changes if rejected)
                        width=1920,
                        height=1080,
                        enhance=False,
                        nologo=True,
                        private=True,
                        safe=False,
                        referrer="pollinations.py"
                    )
                    image = image_model(
                        prompt="A pixel-art, minimalist, black-and-white, line drawing, stick man, simple, clean, no shading, black background, thin lines, round head " + prompt + " art style is retro, pixelated, and reminiscent of 8-bit or 16-bit video game graphics, with clean lines and blocky/pixelated, plain background"
                    )
                    break  # If generation succeeds, exit the retry loop
                except Exception as e:
                    print(f"Attempt {attempt+1} failed to generate image for prompt '{prompt}' with seed {current_seed}: {e}")
                    if attempt < 2:  # If not the last attempt, wait before retrying
                        time.sleep(5)
                    else:
                        print(f"Failed to generate image for prompt '{prompt}' after 3 attempts.")
                        image = None
                        break  # Exit if all attempts fail

            # If image generation succeeded, save it temporarily and ask for approval
            if image is not None:
                try:
                    temp_file = f"./raw/images/temp_{i}.png"
                    image.save(file=temp_file)
                    print(f"Image generated for prompt '{prompt}' with seed {current_seed}. Saved temporarily as {temp_file}.")
                    
                    # Ask user if they're satisfied
                    choice = input("Are you satisfied with this image? (Y/N): ").lower()
                    if choice in ('y', 'yes'):
                        # Rename to final file if satisfied
                        final_file = f"./raw/images/{i}.png"
                        os.rename(temp_file, final_file)
                        print(f"Image approved and saved as {final_file}")
                        satisfied = True
                    else:
                        # Remove temp file, change seed, and regenerate
                        os.remove(temp_file)
                        current_seed = random.randint(0, 4294967295)  # New random seed (max 32-bit unsigned int)
                        print(f"Image rejected. Regenerating with new seed {current_seed}...")
                        time.sleep(2)  # Small delay before retrying
                except Exception as e:
                    print(f"Error handling image for prompt '{prompt}': {e}")
                    os.remove(temp_file) if os.path.exists(temp_file) else None
                    satisfied = True  # Exit loop to avoid infinite retry on save error
            else:
                # If no image was generated, ask to skip or retry
                choice = input("Image generation failed. Skip this prompt? (Y/N): ").lower()
                if choice in ('y', 'yes'):
                    print(f"Skipping prompt '{prompt}'.")
                    satisfied = True
                else:
                    current_seed = random.randint(0, 4294967295)  # New seed for retry
                    print(f"Retrying image generation with new seed {current_seed}...")


"""




def generate_image(prompt, seed, file_path):
    """Generate and save an image for a given prompt and seed."""
    image = None
    for attempt in range(3):  # Try up to 3 times
        try:
            image_model = pollinations.Image(
                model="flux",
                seed=seed,
                width=1920*2,
                height=1080*2,
                enhance=False,
                nologo=True,
                private=True,
                safe=False,
                referrer="pollinations.py"
            )
            image = image_model(
                prompt="minimalist, black-and-white, line drawing, stick figure, simple, clean, no shading, black background,thin lines, round head"+ prompt+"plain background"
            )
            image.save(file=file_path)
            print(f"Generated and saved: {file_path} with seed {seed}")
            return True
        except Exception as e:
            print(f"Attempt {attempt+1} failed for '{prompt}' with seed {seed}: {e}")
            if attempt < 2:
                time.sleep(5)
            else:
                print(f"Failed to generate '{prompt}' after 3 attempts.")
                return False
    return False

def generateImages(prompts):
    main_seed = 3174564238  # Default seed
    image_files = {}  # Store prompt and file info

    # Step 1: Generate all images with the main seed
    print("Generating all images...")
    for i, prompt in enumerate(prompts, start=1):
        file_path = f"./raw/images/{i}.png"
        success = generate_image(prompt, main_seed, file_path)
        if success:
            image_files[i] = {"prompt": prompt, "file": file_path, "seed": main_seed}
        else:
            image_files[i] = {"prompt": prompt, "file": None, "seed": main_seed}

    # Step 2: Ask user which images to regenerate
    while True:
        print("\nAll images generated. Review them in './raw/images/'.")
        print("Files generated:", ", ".join([f"{i}.png" for i in image_files.keys()]))
        regenerate_input = input("Enter the numbers of images to regenerate (e.g., '1 3 5'), or 'done' to finish: ").strip().lower()

        if regenerate_input == "done":
            break

        # Parse input for numbers
        try:
            numbers = [int(num) for num in regenerate_input.split()]
            invalid_numbers = [num for num in numbers if num not in image_files]
            if invalid_numbers:
                print(f"Invalid numbers: {invalid_numbers}. Valid range: 1 to {len(prompts)}")
                continue

            # Regenerate specified images with new seeds
            for num in numbers:
                prompt = image_files[num]["prompt"]
                old_file = image_files[num]["file"]
                new_seed = random.randint(0, 4294967295)  # New random seed

                # Remove old file if it exists
                if old_file and os.path.exists(old_file):
                    os.remove(old_file)

                # Generate new image
                file_path = f"./raw/images/{num}.png"
                success = generate_image(prompt, new_seed, file_path)
                if success:
                    image_files[num] = {"prompt": prompt, "file": file_path, "seed": new_seed}
                else:
                    print(f"Failed to regenerate image {num}. Keeping it as is.")

        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces or 'done'.")
            continue

    print("Process complete.")