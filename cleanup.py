import os

# Define folder paths
images_path = "raw/images"
audios_path = "raw/audios"
subtitles_path = "raw/subtitles"
videos_path = "raw/videos"

# Function to clear the terminal (cross-platform)
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to delete all files in a given folder
def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Main logic
clear_terminal()  # Clear terminal at the start
choice = input("Delete all files in all folders? (Y/N): ").lower()

if choice in ('y', 'yes'):
    # Delete all files in all folders
    print("Deleting all files in all folders...")
    delete_files_in_folder(images_path)
    delete_files_in_folder(audios_path)
    delete_files_in_folder(subtitles_path)
    delete_files_in_folder(videos_path)
    print("All files deleted.")

elif choice in ('n', 'no'):
    # Delete files from specific folders based on user input
    clear_terminal()  # Clear before showing folder options
    print("Choose which folders to delete files from:")

    # Images folder
    img_choice = input("[[Delete]] files in [[images]] folder? (Y/N): ").lower()
    if img_choice in ('y', 'yes'):
        clear_terminal()  # Clear before showing deletion
        delete_files_in_folder(images_path)
        print("Files in images folder deleted.")

    # Audios folder
    clear_terminal()  # Clear before next prompt
    audio_choice = input("[[Delete]] files in [[audios]] folder? (Y/N): ").lower()
    if audio_choice in ('y', 'yes'):
        clear_terminal()  # Clear before showing deletion
        delete_files_in_folder(audios_path)
        print("Files in audios folder deleted.")

    # Subtitles folder
    clear_terminal()  # Clear before next prompt
    sub_choice = input("[[Delete]] files in [[subtitles]] folder? (Y/N): ").lower()
    if sub_choice in ('y', 'yes'):
        clear_terminal()  # Clear before showing deletion
        delete_files_in_folder(subtitles_path)
        print("Files in subtitles folder deleted.")

    # Videos folder
    clear_terminal()  # Clear before next prompt
    video_choice = input("[[Delete]] files in [[videos]] folder? (Y/N): ").lower()
    if video_choice in ('y', 'yes'):
        clear_terminal()  # Clear before showing deletion
        delete_files_in_folder(videos_path)
        print("Files in videos folder deleted.")

else:
    clear_terminal()  # Clear before showing error
    print("Invalid input. Please enter Y or N.")