import tkinter as t
import sys, subprocess
from tkinter.ttk import *
from tkinter import messagebox, filedialog as f
def button_exit(window):
    if messagebox.askquestion("Exit?", "Are you sure you want to exit?") == "yes":
        window.destroy()
        sys.exit()
    else:
        return

def button_file_select(widget_output_entry, output_entry):
    file = t.filedialog.askdirectory()
    output_entry.change_state('normal')
    print(file)
    widget_output_entry.delete(0, "end")
    if file is None and file != "":
        widget_output_entry.insert(0, "C:/")
    else:
        widget_output_entry.insert(0, str(file))
    output_entry.change_state('disabled')
    
def button_about():
    message = "This was a program made by MrHatman26, AKA nobody important."
    message = message + "\n\nWhat is this?: This is a tool that allows you to create your own vigenere tables and use them to cipher and decipher messages."
    message = message + "\n\nThis program was made using Python and uses the following libraries:\n-tkinter: For the GUI\n-sys: For exiting the program"
    message = message + "\n\nCurrent Version: 1.0.0"
    #This is a stupid way to do messages, but whatever
    messagebox.showinfo("About", message)
