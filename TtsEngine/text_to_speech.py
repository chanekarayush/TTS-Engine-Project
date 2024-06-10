"""Hi Mom TTS Engine Module - Say Hi Mom Blazingly Fast"""
__version__ = "1.0.2"
__author__ = "Ayush Chanekar"

import tkinter as tk
import customtkinter as CTk
from pyttsx3 import init
import wave
import os

dirname = os.path.dirname(__file__)
filnam = os.path.join(dirname, 'icon.ico')

filename = ""

# Function to convert text to speech and save to file (if specified)


def get_outputfile(event):
    global filename
    filename = tk.filedialog.asksaveasfilename(
        title="Save WAV File", filetypes=[("MP3 Files", "*.mp3")])
    if not filename.endswith(".mp3"):
        filename += ".mp3"
    fname.set(filename)

    completion_msg.configure(text="")


def write_to_wav(filename=""):
    if filename:
        wavname = filename.replace("mp3", "wav")
        audio = open(filename, 'rb').read()
        params = (2, 2, 11500, 0, 'NONE', 'not compressed')
        with wave.open(wavname, 'wb') as audio_file:
            audio_file.setparams(params)
            audio_file.writeframes(audio)
        try:
            os.remove(filename)
        except Exception as e:
            print(f"An error occurred: {e}")
        completion_msg.configure(
            text=f"File {wavname} has been sucessfully generated")
    return


def speak_and_save():
    engine = init()  # Initialize text-to-speech engine

    text = text_entry.get().strip()
    if not text:
        return

    voices = engine.getProperty('voices')
    selected_voice_id = voice_var.get()

    # Set selected voice
    engine.setProperty('voice', voices[selected_voice_id].id)

    # Ensure the speed slider is set to 1 for normal speed
    speed = speed_scale.get()
    if speed != 1.0:
        rate = engine.getProperty('rate')
        new_rate = int(rate * speed)  # Adjust rate based on slider
        engine.setProperty('rate', new_rate)

    engine.say(text)
    engine.runAndWait()  # Speak the text

    # Save to file if a filename is provided
    if fname.get():
        engine.save_to_file(text, fname.get())
        engine.runAndWait()  # Save the audio
        if wav_output.get():
            write_to_wav(filename=fname.get())
        else:
            completion_msg.configure(
                text=f"File {filename} has been sucessfully generated")

    # Reset button state (optional)
    speak_button.configure(state=tk.NORMAL)
    return

# Function to toggle dark mode/light mode


def toggle_mode():
    if mode_switch.get() == 1:
        CTk.set_appearance_mode("dark")
    else:
        CTk.set_appearance_mode("light")


# Create the main window
root = CTk.CTk()
root.iconbitmap(filnam)
root.minsize(500, 300)
root.title("Text-to-Speech Converter")


# Text input field
text_label = CTk.CTkLabel(master=root, width=10, height=10, text="").pack()
text_label = CTk.CTkLabel(master=root, text="Enter text:",
                          font=("Sans Serif", 16, "bold"))
text_label.pack()

text_entry = CTk.CTkEntry(master=root, width=300,
                          placeholder_text="Text to be read")
text_entry.pack(pady=10)

# Voice selection radio buttons
voice_var = tk.IntVar()  # Variable to store selected voice index
voice_frame = CTk.CTkFrame(master=root)
voice_frame.pack(pady=10)

voice_choices = ["Default"]  # Add default voice option

# Get available voices and populate radio buttons dynamically
voice_label = CTk.CTkLabel(
    master=voice_frame, text="Select voice:", font=("Sans Serif", 14, "bold"))
voice_label.pack()
engine = init()  # Initialize engine temporarily
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    voice_choices.append(voice.name)
    radio_button = CTk.CTkRadioButton(
        master=voice_frame, text=voice.name, variable=voice_var, value=i)
    radio_button.pack(pady=10, padx=10, fill="both")
engine.stop()  # Shut down engine after getting voices

# Speech speed slider
speed_label = CTk.CTkLabel(
    master=root, text="Speech Speed:", font=("Sans Serif", 14))
speed_label.pack()

speed_scale = CTk.CTkSlider(master=root, from_=0.5, to=2, number_of_steps=10)
speed_scale.set(1)  # Default value for normal speed
speed_scale.pack()


# Output file entry
filename_label = CTk.CTkLabel(
    master=root, text="Save to file (optional):", font=("Sans Serif", 14))
filename_label.pack(pady=10)

fname = tk.StringVar()
filename_entry = CTk.CTkEntry(master=root, width=200, textvariable=fname)
filename_entry.bind("<1>", get_outputfile)
filename_entry.pack()

# Speak button
speak_button = CTk.CTkButton(
    master=root, text="Speak & Save (if file provided)", command=speak_and_save)
speak_button.pack(pady=10)


switch_frame = CTk.CTkFrame(master=root)
switch_frame.pack(pady=10)

# WAV output switch
wav_output = tk.IntVar(value=1)
wav_switch = CTk.CTkSwitch(
    master=switch_frame, text="WAV File Output", variable=wav_output, onvalue=1, offvalue=0)
wav_switch.grid(row=0, column=0, padx=10, pady=10)

# Dark mode/light mode switch
mode_var = tk.IntVar(value=1)
mode_switch = CTk.CTkSwitch(
    master=switch_frame, text="Toggle Dark Mode", command=toggle_mode,  onvalue=1,
    offvalue=0, variable=mode_var)
mode_switch.grid(row=0, column=1, padx=10, pady=10)

completion_msg = CTk.CTkLabel(master=root, text_color=("green",
                                                       "lightgreen"), text="", wraplength=400)
completion_msg.pack(padx=10, pady=20)

root.mainloop()
