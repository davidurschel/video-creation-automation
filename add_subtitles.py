import whisper
from moviepy.editor import TextClip, VideoClip, CompositeVideoClip

FONT = "Courier-New-Bold"
FONTSIZE = 16
TEXT_COLOR = "yellow"
TEXT_BG_COLOR = "gray45"
TEXT_STROKE_COLOR = "black"
STROKE_WIDTH = 4
TEXT_OPACITY = 0.4

def transcribe_audio(audio_filepath):
    model = whisper.load_model("base")
    result = model.transcribe(audio_filepath, word_timestamps=True)

    return result["segments"]
    

def combine_words(words:list, end_time:float, text_durration:float=0.8) -> list:
    if len(words)==0: return
    res, temp = [], {"text": "", "start": words[0]["start"], "end": min(words[0]["start"] + text_durration, end_time)}
    for word in words:
        if word["end"] > temp["end"]:
            res.append(temp)
            temp = {"text": word["word"], "start": temp["end"], "end": min(word["start"] + text_durration, end_time)}
            continue
        temp["text"] =  temp["text"] + "\n" + word["word"]
    res.append(temp)
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
        text = seg["text"]
        
        # Generate TextClip object with the specified text
        txtC:VideoClip = TextClip(text, fontsize=FONTSIZE, font=FONT, color=TEXT_COLOR, stroke_color=TEXT_STROKE_COLOR, 
                                  stroke_width=STROKE_WIDTH, size=(vid.size[0]*0.9, None), align='center').set_position("center")
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
