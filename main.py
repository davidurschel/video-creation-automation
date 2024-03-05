from clip_functions import make_clips
from make_script import make_script, get_random_prompt
from generate_audio import generate_audio

def whole_shabang():
    title, script = make_script(prompt=get_random_prompt())
    print(f"Script for '{title}' is finished")
    print("Generating audio...")
    generate_audio(title=title, text=script)
    print(f"Audio for '{title}' is finished")
    print("Making clips")
    make_clips()


while(True):
    print("\nWelcome to the CLI...")
    print("1. Make Clips")
    print("2. Full stuff")
    print("3. Exit")
    choice = input()
    if choice=="1":
        make_clips()
    if choice=="2":
        whole_shabang()
    elif choice=="3":
        exit()


