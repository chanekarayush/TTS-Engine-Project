import pyttsx3
import os
import tts_ui as ui

root = ui.Tk()
app = ui.UserInput(root)
root.mainloop()

reader = pyttsx3.init()
voices = reader.getProperty('voices')

# print("Available Voices")
# for voice in voices:
#     print(f"- {voice.id}")
abs_path = os.path.dirname(__file__)
abs_path += "\\content_path\\TTS_ENGINE.txt"
file = open(abs_path, "r")
content = file.readline()
path = file.readline()
reader.setProperty('voice', voices[1].id)
reader.say(content)
reader.save_to_file(content, path)

reader.runAndWait()
