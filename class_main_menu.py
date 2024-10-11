import tkinter as t
from tkinter.ttk import *
from class_window import *
from class_widgets import *
from tkinter import messagebox
from gui_misc_button_funcs import button_exit, button_about
from misc import res_spec

class MainMenu():
    def __init__(self, resolution, title, resize_horizontal, resize_vertical, v_table):
        self.return_val = 0
        if v_table is not None:
            if len(v_table) == 52:
                self.window = WindowBase(res_spec(900, 910), title, resize_horizontal, resize_vertical, True)
                self.text_height = 40
                self.text_width = 110
            else:
                self.window = WindowBase(resolution, title, resize_horizontal, resize_vertical, True)
                self.text_height = 20
                self.text_width = 100
        else:
            self.window = WindowBase(resolution, title, resize_horizontal, resize_vertical, True)
            self.text_height = 20
            self.text_width = 100
        self.widgets = {
                "label_title": Label(self.window, "What would you like to do?:"),
                "button_generate": Button(self.window, "Generate Vigenere", lambda: self.button_return(0), 20),
                "button_load": Button(self.window, "Load Vigenere", lambda: self.button_return(1), 20),
                "button_cipher": Button(self.window, "Cipher Text", lambda: self.button_return(2), 20),
                "button_decipher": Button(self.window, "Decipher Text", lambda: self.button_return(3), 20),
                "button_about": Button(self.window, "About", lambda: button_about(), 20),
                "button_exit": Button(self.window, "Exit", lambda: button_exit(self.window), 20),
                "label_vigenere_table": Label(self.window, "Loaded Vigenere Table:"),
                "textfield_loaded_vigenere": Textbox(self.window, "No vigenere table loaded.", self.text_width, self.text_height)
            }
        if v_table is not None:
            self.widgets["textfield_loaded_vigenere"].delete(1.0, "end")
            for line in v_table:
                self.widgets["textfield_loaded_vigenere"].insert("end", line)
                self.widgets["textfield_loaded_vigenere"].insert("end", "\n")
        self.widgets["textfield_loaded_vigenere"].make_centre()

    def pack_and_run(self):
        for widget in self.widgets.values():
            try:
                widget.pack(pady=4)
            except:
                pass
        self.window.mainloop()
        return self.return_val

    def button_return(self, return_val):
        self.return_val = return_val
        print("destroy")
        self.window.destroy()
        self.window = None
