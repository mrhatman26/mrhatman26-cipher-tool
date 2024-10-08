import tkinter as t
import traceback
from tkinter.ttk import *
from class_window import *
from class_widgets import *
from misc import *

class DecipherWindow():
    def __init__(self, resolution, title, resize_horizontal, resize_vertical, v_table):
        self.window = WindowBase(resolution, title, resize_horizontal, resize_vertical, False)
        self.window.withdraw()
        self.v_table = v_table
        self.widgets = None
        self.message = ""
        self.deciphered_text = ""
        self.key = ""
        self.new_key = ""
        if ask_question("Load File?", "Would you like to load a text file to decipher?") is True:
            self.message_file = load_file()
            if self.message_file is None:
                show_warning("No FilE", "No file was selected, please enter your message instead.")
                self.widget_switch(False)
            else:
                self.message = []
                for line in self.message_file:
                    self.message.append(line.upper())
                self.message_file.close()
                self.widget_switch(True)
        else:
            self.message_file = None
            self.return_val = 0
            self.widget_switch(False)

    def pack_and_run(self):
        self.window.deiconify()
        for key, widget in self.widgets.items():
            widget.pack(pady=5)
        self.window.mainloop()

    def widget_switch(self, key_window):
        if self.widgets is not None:
            for key, widget in self.widgets.items():
                widget.pack_forget()
        if key_window is True:
            self.window.geometry(res_spec(600, 100))
            self.widgets = {
                    "label_key": Label(self.window, "Please enter a key: "),
                    "entry_cipher_key": Entry(self.window, "center", 40),
                    "button_start_cipher": Button(self.window, "Start Cipher", lambda: self.button_start_decipher(), 20)
                }
        else:
            self.widgets = {
                    "label_title": Label(self.window, "Please enter your cipher text:"),
                    "entry_cipher_text": Entry(self.window, "center", 40),
                    "label_key": Label(self.window, "Please enter a key: "),
                    "entry_cipher_key": Entry(self.window, "center", 40),
                    "button_start_cipher": Button(self.window, "Start Cipher", lambda: self.button_start_decipher(), 20)
                }

    def button_start_decipher(self):
        conjoined_deciphered_text = ""
        if self.message == "":
            if self.widgets["entry_cipher_text"].get() == "":
                show_error("No Message", "No message was given to decipher, please try again.")
            else:
                self.message = self.widgets["entry_cipher_text"].get()
                self.button_start_decipher()
        elif self.widgets["entry_cipher_key"].get() == "":
            show_warning("No Key", "Please enter a key to cipher your message.")
        else:
            self.key = self.widgets["entry_cipher_key"].get().upper()
            self.new_key = keygen(self.message, self.widgets["entry_cipher_key"].get().upper())
            if type(self.message) == list:
                self.deciphered_text = []
                for line in self.message:
                    print(line)
                    self.new_key = keygen(line, self.key)
                    self.deciphered_text.append(self.decipher(line, self.new_key))
            else:
                self.new_key = keygen(self.message, self.key)
                self.deciphered_text = self.decipher(self.message, self.new_key)
            if type(self.deciphered_text) == str:
                show_message("Decipher Complete", "Deciphere text complete. Your text is now:\n" + self.deciphered_text)
            else:
                for line in self.deciphered_text:
                    conjoined_deciphered_text = conjoined_deciphered_text + line
                show_message("Decipher Complete", "Deciphere text complete. Your text is now:\n" + conjoined_deciphered_text)
            if ask_question("Save Decipher?", "Would you like to save your deciphered text to a file?") is True:
                if type(self.message) == str:
                    if save_file(self.deciphered_text) is True:
                        show_message("Saved", "Deciphered text has been saved")
                    else:
                        show_warning("Not Saved", "Warning: Deciphered text has not been saved.")
                else:
                    if save_file(conjoined_deciphered_text) is True:
                        show_message("Saved", "Deciphered text has been saved")
                    else:
                        show_warning("Not Saved", "Warning: Deciphered text has not been saved.")
            self.end_window()

    def end_window(self):
        self.window.destroy()

    def decipher(self, message, new_key):
        deciphered_text = ""
        letter_no = 0
        for key_letter in new_key:
            line_no = 0
            for line in self.v_table:
                if line[0] == key_letter:
                    break
                line_no += 1
            try:
                if message[letter_no] != "\n":
                    line_index = self.v_table[line_no].index(message[letter_no])
                    print("Changing " + key_letter + " to " + self.v_table[0][line_index])
                    deciphered_text = deciphered_text + self.v_table[0][line_index]
                else:
                    deciphered_text = deciphered_text + message[letter_no]
            except Exception:
                deciphered_text = deciphered_text + message[letter_no]
            letter_no += 1
        return deciphered_text
            
