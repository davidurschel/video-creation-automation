import whisper
from moviepy.editor import TextClip, VideoClip, CompositeVideoClip
from textwrap import wrap

FONT = "Courier-New-Bold"
FONTSIZE = 64
TEXT_COLOR = "white"
TEXT_BG_COLOR = "#10436e"
TEXT_STROKE_COLOR = "black"
STROKE_WIDTH = 2.5
TEXT_BG_OPACITY = 0.3

def transcribe_audio(audio_filepath):
    model = whisper.load_model("base")
    result = model.transcribe(audio_filepath, word_timestamps=True)

    return result["segments"]
    

def combine_words(words:list, end_time:float, text_durration:float=0.9) -> list:
    if len(words)==0: return
    res, temp_words, temp_starts, temp_ends = [], [], [], []
    for i, word in enumerate(words):
        if i == 0:
            temp_words, temp_starts, temp_ends = [word["word"]], [word["start"]], [min(word["end"] + text_durration, end_time)]
            curr_start = temp_starts[0]
            continue

        while len(temp_ends) > 0 and word["start"] > temp_ends[0]:
            res.append({"text":" ".join(temp_words).strip(), "start":curr_start, "end":temp_ends[0]})
            temp_starts.pop(0)
            curr_start = temp_ends.pop(0)
            temp_words.pop(0)

        res.append({"text":" ".join(temp_words).strip(), "start":curr_start, "end":word["start"]})
        temp_words.append(word["word"])
        temp_starts.append(word["start"])
        temp_ends.append(min(word["end"] + text_durration, end_time))
        curr_start = word["start"]
    
    while len(temp_words) > 0:
        res.append({"text":" ".join(temp_words).strip(), "start":curr_start, "end":temp_ends[0]})
        curr_start = temp_ends.pop(0)
        temp_words.pop(0)
        
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
        
        # Generate TextClip object with the specified text
        txtC:VideoClip = TextClip(text, fontsize=FONTSIZE, font=FONT, color=TEXT_COLOR, stroke_color=TEXT_STROKE_COLOR, 
                                  stroke_width=STROKE_WIDTH, align='center').set_position('center')
        txtC = txtC.set_start(start_time)
        txtC = txtC.set_duration(end_time - start_time)
        return txtC

    # Create TextClip objects for each caption segment
    caption_clips = []
    for seg in segs:
        caption_clips.append(generate_caption(seg))

    # Create a CompositeVideoClip with the original video and caption clips
    final_clip:VideoClip = CompositeVideoClip([vid] + caption_clips)

    return final_clip
