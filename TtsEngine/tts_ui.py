from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os



class UserInput:
    def __init__(self, window) -> None:
        self.root = window
        self.root.title("Text to Speech Engine")
        self.root.resizable(False, False)

        self.final_content = ""

        # Content section
        self.frame = ttk.Frame(self.root)
        self.frame.grid(sticky="nsew")

        self.frame1 = ttk.Labelframe(self.frame, text="Audio Contents")
        self.frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label1 = ttk.Label(self.frame1, text="Enter the Text to be converted to speech")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.content = ttk.Entry(self.frame1)
        self.content.grid(row=1, column=0, padx=10, pady=10, sticky="ew")


        # Audio File name and path
        self.frame2 = ttk.Labelframe(self.frame, text="Save File")
        self.frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # File path and submit file
        self.file_label = ttk.Label(self.frame2, text="Enter File Destination and Name:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10)

        self.file_entry = ttk.Label(self.frame2)
        self.file_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.file_button = ttk.Button(self.frame2, text="Choose File", command=self.choose_file_destination)
        self.file_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.submit_data = ttk.Button(self.frame2, text="Submit & Exit", command=self.submit_all)
        self.submit_data.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Configures fonts and text family
        for widget in self.frame1.winfo_children():
            if isinstance(widget, ttk.Button) or isinstance(widget, ttk.Entry):
                continue
            widget['font'] = ("Sans Serif", 12, "bold")
            
        for widget in self.frame2.winfo_children():
            if isinstance(widget, ttk.Button) or isinstance(widget, ttk.Entry):
                continue
            widget['font'] = ("Sans Serif", 12, "bold")

        # Configures column and row weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def choose_file_destination(self):
        # Opens the file dialog to choose file destination
        global file_destination
        file_destination = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("MP3 files", "*.mp3"), ("All files", "*.*")],
            title="Save Audio File"
        )

        if file_destination:
            self.file_entry['text'] = file_destination
    def submit_all(self):
        try:
            if file_destination and self.content.get():
                messagebox.showinfo("Information", message="Your text has been submitted and a file will be generated shortly.")
                self.write_data()
                self.root.destroy()
            elif self.content.get() == "":
                messagebox.showerror("Error", message="Please Enter Text to be Converted")
            else:
                messagebox.showerror("Error", message="Please Enter File Name and Destination Folder in the dialog box")
        
        except NameError:
            # File name wasn't selected which is why it maybe undefined
            messagebox.showerror("Error", message="Please Enter File Name and Destination Folder in the dialog box")
    def write_data(self):
                abs_path = os.path.dirname(__file__)
                abs_path += "\\content_path\\TTS_ENGINE.txt"
                file = open(abs_path, "w")
                file.write(self.content.get())
                file.write("\n")
                file.write(file_destination)
                file.close()


# if __name__ == "__main__":
#     root = Tk()
#     # root.iconbitmap("mic_icon.ico")
#     # Tried to use icon but failed :-/
#     app = UserInput(root)
#     root.mainloop()
