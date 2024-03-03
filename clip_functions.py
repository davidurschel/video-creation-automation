from moviepy.editor import VideoFileClip, AudioFileClip, VideoClip, AudioClip
from random import randint, random
import time
import shutil
import os
from random import randrange
from math import floor


NEW_TTS_FILEPATH = "video_files/new_tts_inputs/"
USED_TTS_FILEPATH = "video_files/used_tts_inputs/"
OUTPUT_FILEPATH = "video_files/outputs/"
BACKGROUND_VIDEO_FILEPATH = "video_files/background_video_files/"

def combine_clips(videoFilePath:str, audioFilePath:str) -> VideoClip:
    vid:VideoClip = VideoFileClip(videoFilePath).without_audio()
    vidDur = vid.duration

    aud:AudioClip = AudioFileClip(audioFilePath)
    audDur = aud.duration

    vidStartTime = random() * (vidDur-audDur)
    print(vidStartTime)
    vid = vid.subclip(vidStartTime, vidStartTime+audDur)
    
    res = vid.set_audio(aud)
    return res

def save_clip(clip:VideoFileClip, clipName:str, codec:str=".mp4"):
    clip.write_videofile(clipName+codec, fps=60)

def make_clips():
    bg_files = os.listdir(BACKGROUND_VIDEO_FILEPATH)

    for input_tts in os.listdir(NEW_TTS_FILEPATH):
        print(BACKGROUND_VIDEO_FILEPATH + input_tts)
        clip1 = combine_clips(BACKGROUND_VIDEO_FILEPATH + bg_files[floor(randrange(len(bg_files)))], NEW_TTS_FILEPATH + input_tts)
        output_filename = "Youtube_Short_" + str(time.time())

        codec = ".mp4"
        save_clip(clip1, output_filename, codec=codec)

        # Move the file to the output folder1
        dst = USED_TTS_FILEPATH + input_tts
        print(dst)
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(output_filename + codec, OUTPUT_FILEPATH)
        shutil.move(NEW_TTS_FILEPATH + input_tts, USED_TTS_FILEPATH)
    else:
        print("\nNo source audio available")