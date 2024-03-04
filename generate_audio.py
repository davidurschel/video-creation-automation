import pyttsx3

title = input("title: ")
text = input("text: ")

engine = pyttsx3.init()

engine.save_to_file(text, title + '.wav')
engine.runAndWait()