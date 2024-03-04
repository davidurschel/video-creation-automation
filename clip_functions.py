from moviepy.editor import VideoFileClip, AudioFileClip, VideoClip, AudioClip, TextClip
from random import randint, random
import time
import shutil
import os
from random import randrange
from math import floor
from add_subtitles import add_subtitles

NEW_TTS_FILEPATH = "video_files/new_tts_inputs/"
USED_TTS_FILEPATH = "video_files/used_tts_inputs/"
OUTPUT_FILEPATH = "video_files/outputs/"
BACKGROUND_VIDEO_FILEPATH = "video_files/background_video_files/"

def combine_clips(video_filepath:str, audio_filepath:str, subtitles_on:bool=True) -> VideoClip:
    vid:VideoClip = VideoFileClip(video_filepath).without_audio()
    vid_dur = vid.duration

    aud:AudioClip = AudioFileClip(audio_filepath)
    aud_dur = aud.duration

    vid_start_time = random() * (vid_dur-aud_dur)
    print(vid_start_time)
    vid = vid.subclip(vid_start_time, vid_start_time+aud_dur)
    

    res = vid.set_audio(aud)

    # Get the transcript and and set the subtitles
    if subtitles_on:
        res = add_subtitles(res, audio_filepath)

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

        # Move the file to the output folder
        dst = USED_TTS_FILEPATH + input_tts
        print(dst)
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(NEW_TTS_FILEPATH + input_tts, USED_TTS_FILEPATH)

        shutil.move(output_filename + codec, OUTPUT_FILEPATH)
        
    else:
        print("\nNo source audio available")

if __name__ == "__main__":
    make_clips()
    
