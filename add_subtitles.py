import whisper
from moviepy.editor import TextClip, VideoClip, CompositeVideoClip
from textwrap import wrap
from random import random

FONT = "Segoe-UI-Bold"
FONTSIZE = 128
TEXT_COLOR = "white"
TEXT_ALT_COLOR = "yellow"
TEXT_ALT_FREQ = 0.3
TEXT_BG_COLOR = "#10436e"
TEXT_STROKE_COLOR = "black"
STROKE_WIDTH = 4.0
TEXT_BG_OPACITY = 0.3
ZOOM_DURATION = 0.1
INITIAL_SCALE = 0.8
FINAL_SCALE = 1.0

def transcribe_audio(audio_filepath):
    model = whisper.load_model("base")
    result = model.transcribe(audio_filepath, word_timestamps=True)

    return result["segments"]
    

def combine_words(words:list, end_time:float, text_durration:float=0.5) -> list:
    if len(words)==0: return
    res, curr_start, temp_words = [], 0, []
    for i, word in enumerate(words):
        if len(temp_words):
            if curr_start + text_durration > word["end"]:
                temp_words.append(word["word"])
                continue
            else:
                res.append({"text":" ".join(temp_words), "start":curr_start, "end":min(curr_start + text_durration, word["start"])})
        curr_start = word["start"]
        temp_words = [word["word"]]
        if i == len(words)-1:
            res.append({"text":" ".join(temp_words), "start":curr_start, "end":word["end"]})
    return res
        

def add_subtitles(vid:VideoClip, audio_filepath:str) -> VideoClip:
    segs = transcribe_audio(audio_filepath)

    words = []
    for seg in segs:
        words += seg["words"]

    segs = combine_words(words, vid.duration)
    
    def generate_caption(seg):
        start_time = seg["start"]
        end_time = seg["end"]
        text = "\n".join(wrap(seg["text"], 16))
        text = text or " "
        fontsize = int(FONTSIZE*vid.size[0]/1080)
        
        # Generate TextClip object with the specified text
        text_color = (TEXT_COLOR if random() > TEXT_ALT_FREQ else TEXT_ALT_COLOR)
        txtC:TextClip = TextClip(text, fontsize=fontsize, font=FONT, color=text_color, stroke_color=TEXT_STROKE_COLOR, 
                                  stroke_width=STROKE_WIDTH, align='center').set_position('center')
        txtC = txtC.set_start(start_time)
        txtC = txtC.set_duration(end_time - start_time)

        def resize(t):
            # Calculate the scaling factor based on elapsed time and total duration
            scale_factor = min(INITIAL_SCALE + t/ZOOM_DURATION * (FINAL_SCALE - INITIAL_SCALE), FINAL_SCALE)
            return scale_factor

        res:VideoClip = txtC.resize(lambda t: resize(t))
        return res

    # Create TextClip objects for each caption segment
    caption_clips = []
    for seg in segs:
        caption_clips.append(generate_caption(seg))

    # Create a CompositeVideoClip with the original video and caption clips
    final_clip:VideoClip = CompositeVideoClip([vid] + caption_clips)

    return final_clip

if __name__ == "__main__":
    fonts = TextClip.list('font')
    for f in fonts:
        if "bold" in f.lower():
            print(f)
