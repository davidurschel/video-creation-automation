from moviepy.editor import VideoFileClip, AudioFileClip, VideoClip, AudioClip
from random import randint, random


def combine_clips(videoFilePath:str, audioFilePath:str) -> VideoClip:
    vid:VideoClip = VideoFileClip(videoFilePath).without_audio()
    vidDur = vid.duration

    aud:AudioClip = AudioFileClip(audioFilePath)
    audDur = aud.duration

    vidStartTime = random() * (vidDur-audDur)
    print(vidStartTime)
    vid = vid.subclip(vidStartTime, vidStartTime+audDur)
    
    
    res = vid.set_audio(aud)
    

    return res #.set_audio(audioClip)

def save_clip(clip:VideoFileClip, clipName:str, codec:str=".mp4"):
    clip.write_videofile(clipName+codec, fps=60)