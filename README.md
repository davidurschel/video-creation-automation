# Video Creation Automation

Automatically creates videos with AI voiceover for Youtube shorts and TikToks with Subtitles. Import your own audio, video, script, or let everything be handled by an LLM such as `LLaMa2` ran through `OLLaMa`. Check out some sample outputs here: https://www.youtube.com/channel/UC8mYA_6kYQrLjPakonXC_Iw

## Running Instructions

### Setup

Install ImageMagick application:

```https://imagemagick.org/script/download.php```

Install Python 3.8:

```https://www.python.org/downloads/release/python-380/```

Install required dependancies:

```pip install -r requirements.txt```

Setup Input and Output Folder:

```python3 setup_folders.py```

### Running

Paste background video clips into:

```video_files/background_video_files```

If you want to use your own script, paste files into:

```video_files/input_txt_files```

If you want to use your own audio, paste files into:

```video_files/new_tts_inputs```

Run from command:

```python3 main.py```

Your outputs will be found in:

```video_files/new_tts_inputs```

Follow CLI usage instructions
