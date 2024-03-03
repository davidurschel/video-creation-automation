import time
import shutil
import os
from clip_functions import combine_clips, save_clip
from random import randrange
from math import floor

NEW_TTS_FILEPATH = "video-creation-automation/video_files/new_tts_inputs/"
USED_TTS_FILEPATH = "video-creation-automation/video_files/used_tts_inputs/"
OUTPUT_FILEPATH = "video-creation-automation/video_files/outputs/"
BACKGROUND_VIDEO_FILEPATH = "video-creation-automation/video_files/background_video_files/"


bg_files = os.listdir(BACKGROUND_VIDEO_FILEPATH)


for input_tts in os.listdir(NEW_TTS_FILEPATH):
    print(BACKGROUND_VIDEO_FILEPATH + input_tts)
    clip1 = combine_clips(BACKGROUND_VIDEO_FILEPATH + bg_files[floor(randrange(len(bg_files)))], NEW_TTS_FILEPATH + input_tts)
    output_filename = "Youtube_Short_" + str(time.time())

    codec = ".mp4"
    save_clip(clip1, output_filename, codec=codec)

    # Move the file to the output folder
    shutil.move(output_filename + codec, OUTPUT_FILEPATH)
    shutil.move(NEW_TTS_FILEPATH + input_tts, USED_TTS_FILEPATH)




