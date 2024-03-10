from clip_functions import make_clips
from make_script import make_script, get_random_prompt
from generate_audio import generate_audio
import time
import os
from string import ascii_letters

def whole_shabang(title:str, script:str):
    print("Generating audio...")
    generate_audio(title=title, text=script)
    print(f"Audio for '{title}' is Finished")
    print("Making clips...")
    make_clips()
    return

def get_text_source(directory):
    text = []
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Check if the file is a text file
        if os.path.isfile(filepath) and filename.endswith('.txt'):
            # Read the content of the text file
            with open(filepath, 'r') as file:
                content = file.read()
                text.append((filename[:-4], ''.join([char for char in content if char in (ascii_letters + " .?,!1234567890\n")])))
    return text


while(True):
    print("\nWelcome to the CLI...")
    print("1. Make Clips")
    print("2. Automatic Generation")
    print("3. Make From Text")
    print("e - Exit")
    choice = input()
    if choice=="1":
        make_clips()
    elif choice=="2":
        start = time.time()
        title, script = make_script(prompt=get_random_prompt())
        whole_shabang(title, script)
        end = time.time()
        print(end-start)
    elif choice=="3":
        text_sources = get_text_source("video_files/input_txt_files/")
        for ts in text_sources:
            whole_shabang(ts[0], ts[1])
    elif choice=="e":
        exit()


