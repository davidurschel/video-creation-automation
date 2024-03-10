import os

# List of directories to create
directories = ['video_files',
               'video_files/audio_tts_results',
               'video_files/new_tts_inputs',
               'video_files/used_tts_inputs',
               'video_files/background_video_files',
               'video_files/input_txt_files',
               'video_files/outputs',
               'video_files/used_shorts_videos'
               ]

# Loop through the list and create directories if they do not exist
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")
