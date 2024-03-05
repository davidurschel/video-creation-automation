import pyttsx3
import shutil
import os

NEW_TTS_FILEPATH = "video_files/new_tts_inputs/"

def generate_audio(title:str, text:str):
    engine = pyttsx3.init()
    engine.save_to_file(text, title + '.wav')
    engine.runAndWait()

    dst = NEW_TTS_FILEPATH + title + '.wav'
    if os.path.exists(dst):
        os.remove(dst)
    shutil.move(title + '.wav', NEW_TTS_FILEPATH)
    return