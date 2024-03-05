from clip_functions import make_clips
from make_script import make_script, random_prompt
from generate_audio import generate_audio


while(True):
    print("\nWelcome to the CLI...")
    print("1. Make Clips")
    print("2. Full stuff")
    print("3. Exit")
    choice = input()
    if choice=="1":
        make_clips()
    if choice=="2":
        title, script = make_script(prompt=random_prompt())
        generate_audio(title=title, text=script)
        make_clips()
    elif choice=="3":
        exit()


