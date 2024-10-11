import tkinter as t
from tkinter.ttk import *
from class_window import *
from class_widgets import *
from misc import *

class CipherWindow():
    def __init__(self, resolution, title, resize_horizontal, resize_vertical, v_table):
        self.window = WindowBase(resolution, title, resize_horizontal, resize_vertical, False)
        self.v_table = v_table
        self.window.withdraw()
        self.widgets = None
        self.message = ""
        self.cipher_text = ""
        self.key = ""
        self.new_key = ""
        if ask_question("Load File?", "Would you like to load a text file to cipher?") is True:
            self.message_file = load_file()
            if self.message_file is None:
                show_warning("No File", "No file was selected, please enter your message instead.")
                self.widget_switch(False)
            else:
                self.message = []
                for line in self.message_file:
                    self.message.append(line)#.upper())
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
            for widget in self.widgets:
                widget.pack_forget()
        if key_window is True:
            self.window.geometry(res_spec(600, 100))
            self.widgets = {
                    "label_key": Label(self.window, "Please enter a key: "),
                    "entry_cipher_key": Entry(self.window, "center", 40),
                    "button_start_cipher": Button(self.window, "Start Cipher", lambda: self.button_start_cipher(), 20)
                }
        else:
            self.widgets = {
                    "label_title": Label(self.window, "Please enter your cipher text:"),
                    "entry_cipher_text": Entry(self.window, "center", 40),
                    "label_key": Label(self.window, "Please enter a key: "),
                    "entry_cipher_key": Entry(self.window, "center", 40),
                    "button_start_cipher": Button(self.window, "Start Cipher", lambda: self.button_start_cipher(), 20)
                }

    def button_start_cipher(self):
        conjoined_cipher_text = ""
        if self.message == "":
            if self.widgets["entry_cipher_text"].get() == "":
                show_error("No Message", "No message was given to cipher, please try again.")
            else:
                self.message = self.widgets["entry_cipher_text"].get()
                self.button_start_cipher()
        elif self.widgets["entry_cipher_key"].get() == "":
            show_warning("No Key", "Please enter a key to cipher your message.")
        else:
            self.key = self.widgets["entry_cipher_key"].get()
            self.new_key = keygen(self.message, self.widgets["entry_cipher_key"].get())
            if type(self.message) == list:
                self.cipher_text = []
                for line in self.message:
                    print(line)
                    self.new_key = keygen(line, self.key)
                    self.cipher_text.append(self.cipher(line, self.new_key))
            else:
                self.new_key = keygen(self.message, self.key)
                self.cipher_text = self.cipher(self.message, self.new_key)
            if type(self.cipher_text) == str:
                show_message("Cipher Complete", "Cipher is complete. Your text is now:\n" + self.cipher_text)
            else:
                for line in self.cipher_text:
                    conjoined_cipher_text = conjoined_cipher_text + line
                show_message("Cipher Complete", "Cipher is complete. Your text is now:\n" + conjoined_cipher_text)
            if ask_question("Save Cipher?", "Would you like to save your ciphered text to a file?") is True:
                if type(self.message) == str:
                    if save_file(self.cipher_text) is True:
                        show_message("Saved", "Ciphered text has been saved")
                    else:
                        show_warning("Not Saved", "Warning: Ciphered text has not been saved.")
                else:
                    if save_file(conjoined_cipher_text) is True:
                        show_message("Saved", "Ciphered text has been saved")
                    else:
                        show_warning("Not Saved", "Warning: Ciphered text has not been saved.")
            print(self.key)
            print(self.new_key)
            self.end_window()
            
    def cipher(self, message, new_key):
        cipher_text = ""
        letter_no = 0
        for letter in message:
            print("Current letter is: " + letter)
            line_no = 0
            for line in self.v_table:
                #print("Does " + line[0] + " equal " + letter + "?")
                if line[0] == letter:
                    #print("Yes, it does!")
                    break
                #print("No, it doesn't")
                line_no += 1
            try:
                line_index = self.v_table[0].index(new_key[letter_no])
                print("Changing " + letter + " to " + self.v_table[line_no][line_index] + " using the key of " + new_key[letter_no])
                cipher_text = cipher_text + self.v_table[line_no][line_index]
            except:
                cipher_text = cipher_text + letter
            letter_no += 1
        return cipher_text

    def end_window(self):
        self.window.destroy()
