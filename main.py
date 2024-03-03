from clip_functions import make_clips
from upload_functions import upload_video

while(True):
    print("\nWelcome to the CLI...")
    print("1. Make Clips")
    print("2. ")
    print("3. Exit")
    choice = input()
    if choice=="1":
        make_clips()
    elif choice=="3":
        exit()




