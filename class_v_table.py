import tkinter as t
from tkinter.ttk import *
from class_window import *
from class_widgets import *
from tkinter import messagebox
from gui_misc_button_funcs import button_exit, button_about
from misc import *

#VTable Creation
class VTableCreation():
    def __init__(self, resolution, title, resize_horizontal, resize_vertical):
        self.alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.new_alphabet = self.alphabet
        self.shift_alphabet = self.alphabet
        self.key = ""
        self.v_table = []
        self.window = WindowBase(resolution, title, resize_horizontal, resize_vertical, False)
        self.widgets = {
                "label_key": Label(self.window, "Please enter a key for the vigenere table:"),
                "entry_key": Entry(self.window, "center", 20),
                "button_submit": Button(self.window, "Submit", lambda: self.button_submit(), 20)
            }

    def pack_and_run(self):
        for key, widget in self.widgets.items():
            print(key)
            widget.pack(pady=5)
        self.window.mainloop()
        return self.v_table

    def button_submit(self):
        if self.widgets["entry_key"].get() == "":
            show_message("No Key", "Please enter a key.")
        else:
            self.key = self.widgets["entry_key"].get().upper()
            x = 0
            for letter in self.key:
                self.new_alphabet.insert(x, self.new_alphabet.pop(self.new_alphabet.index(letter)))
                x += 1
            self.shift_alphabet = self.new_alphabet
            x = 0
            while x < 26:
                self.v_table.append(self.shift_alphabet.copy())
                self.shift_alphabet.append(self.shift_alphabet.pop(0))
                x += 1
            if ask_question("Save?", "Would you like to save the vigenere table?\n(If no, the table will still be loaded)") is True:
                if save_file(self.v_table) is True:
                    show_message("Saved", "Vigenere table saved successfully.")
                    self.end_window()
                else:
                    show_warning("Unsaved", "Warning: Vigenere table has NOT been saved.")
            else:
                self.end_window()

    def end_window(self):
        self.window.destroy()

#Vtable Loading
def VTableLoading():
    v_table_file = load_file()
    if v_table_file is None:
        show_error("No File Selected", "Error: No file has been selected. Please try again.")
        return None
    else:
        try:
            v_table = []
            for line in v_table_file:
                v_table_line = []
                for letter in line:
                    if letter != "\n":
                        v_table_line.append(letter)
                v_table.append(v_table_line)
            v_table_file.close()
        except Except as e:
            show_error("File Read Error", "The following error occurred when trying to read the selected file:\n" + str(e))
            return None
        try:
            if v_table is None or len(v_table) == 0:
                show_error("File Empty", "Error: file is either empty or does not exist.")
                return None
            else:
                for line in v_table:
                    if len(line) != 26:
                        show_error("Line Length Error", "Error: All lines of the vigenere table must be 26 letters long.")
                        return None
                if len(v_table) != 26:
                    show_error("Vigenere Table Length Error", "Error: The vigenere table must be 26 lines long.")
                    return None
                #show_message("Load Successful", "Vigenere table loaded successfully")
                return v_table
        except Exception as e:
            show_error("Vigenere Table Check Error", "The following error occurred when checking the vigenere table:\n" + str(e))
            return None
