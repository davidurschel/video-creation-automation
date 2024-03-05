import whisper
from moviepy.editor import TextClip, VideoClip, CompositeVideoClip

FONT = "Courier-New-Bold"
FONTSIZE = 32
TEXT_COLOR = "black"
TEXT_BG_COLOR = "gray45"
TEXT_STROKE_COLOR = "white"
STROKE_WIDTH = 2
TEXT_OPACITY = 0.4

def transcribe_audio(audio_filepath):
    model = whisper.load_model("base")
    result = model.transcribe(audio_filepath, word_timestamps=True)

    segs = result["segments"]
    words = []
    for seg in segs:
        words += seg["words"]

    return combine_words(words)

def combine_words(words:list, text_durration:float=0.8) -> list:
    if len(words)==0: return
    res, temp = [], {"text": "", "start": words[0]["start"], "end": words[0]["start"] + text_durration}
    for word in words:
        if word["end"] > temp["end"]:
            res.append(temp)
            temp = {"text": word["word"], "start": temp["end"], "end": word["start"] + text_durration}
            continue
        temp["text"] =  temp["text"] + " " + word["word"]
    return res
        

def add_subtitles(vid, audio_filepath):
    segs = transcribe_audio(audio_filepath)
    
    def generate_caption(seg):
        start_time = seg["start"]
        end_time = seg["end"]
        text = seg["text"]
        
        # Generate TextClip object with the specified text
        txtC:VideoClip = TextClip(text, fontsize=FONTSIZE, font=FONT, color=TEXT_COLOR, stroke_color=TEXT_STROKE_COLOR, 
                                  stroke_width=STROKE_WIDTH, size=(vid.size[0]*0.9, None)).set_position('center')
        txtCbg:VideoClip = TextClip(text, fontsize=FONTSIZE, font=FONT, color=TEXT_COLOR, stroke_color=TEXT_STROKE_COLOR, 
                                  bg_color=TEXT_BG_COLOR, stroke_width=STROKE_WIDTH, 
                                  size=(vid.size[0], None)).set_position('center')
        txtC, txtCbg = txtC.set_start(start_time), txtCbg.set_start(start_time)
        txtC, txtCbg = txtC.set_duration(end_time - start_time), txtCbg.set_duration(end_time - start_time)
        txtCbg:TextClip = txtCbg.set_opacity(TEXT_OPACITY)
        return [txtC, txtCbg]

    # Create TextClip objects for each caption segment
    caption_clips = []
    for seg in segs:
        caption_clips += generate_caption(seg)

    # Create a CompositeVideoClip with the original video and caption clips
    final_clip:VideoClip = CompositeVideoClip([vid] + caption_clips)

    return final_clip
