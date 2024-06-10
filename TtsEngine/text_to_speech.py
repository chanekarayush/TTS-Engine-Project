"""Hi Mom TTS Engine Module - Say Hi Mom Blazingly Fast!!"""
__version__ = "1.0.1"
__author__ = "Ayush Chanekar"


import pyttsx3
import tts_ui as ui

root = ui.Tk()
app = ui.UserInput(root)
root.mainloop()

reader = pyttsx3.init()
voices = reader.getProperty('voices')

# print("Available Voices")
# for voice in voices:
#     print(f"- {voice.id}")
file = open(ui.abs_path, "r")
content = file.readline()
path = file.readline()
reader.setProperty('voice', voices[1].id)
reader.say(content)
reader.save_to_file(content, path)

reader.runAndWait()
