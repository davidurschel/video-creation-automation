import pyttsx3
import shutil
import os

NEW_TTS_FILEPATH = "video_files/new_tts_inputs/"

def generate_audio(title:str, text:str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('pitch', 1.1)
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    # voices = engine.getProperty('voices')
    engine.save_to_file(text, title + '.wav')
    engine.runAndWait()

    dst = NEW_TTS_FILEPATH + title + '.wav'
    if os.path.exists(dst):
        os.remove(dst)
    shutil.move(title + '.wav', NEW_TTS_FILEPATH)

    return