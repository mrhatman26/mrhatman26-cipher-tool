import tkinter as t
from tkinter import filedialog as f
from tkinter import messagebox

def str_to_int_test(text):
    if type(text) == str:
        try:
            return int(text)
        except:
            return False
    else:
        return False

def res_spec(width, height):
    if type(width) != int or type(height) != int:
        width = str_to_int_test(width)
        if width is False:
            raise Exception("width is NOT an integer")
        height = str_to_int_test(height)
        if height is False:
            raise Exception("height is NOT an integer")
    return str(width) + "x" + str(height)

def zlen(item):
    return len(item) - 1

def display_list_pos(list_item, pos, new_line):
    for item in list_item:
        print(item, end="")
    i = 0
    print("\n", end="")
    while True:
        if i != pos:
            print(" ", end="")
        else:
            if new_line is True:
                print("^")
            else:
                print("^", end="")
            return
        i += 1

def display_list_pos_multiline(list_item, pos_x, pos_y):
    y = 0
    for item in list_item:
        if y == pos_y:
            display_list_pos(item, pos_x, False)
        else:
            for letter in item:
                print(letter, end="")
        y += 1
        print("\n", end="")

def load_file():
    window = t.Tk()
    window.withdraw()
    file = t.filedialog.askopenfile(mode="r", filetypes=[("Text File", "*.txt")])
    window.destroy()
    if file is None:
        print("No file selected")
        return None
    else:
        print("File selected: " + str(file.name))
        return file

def save_file(data):
    window = t.Tk()
    window.withdraw()
    save_file = t.filedialog.asksaveasfile(filetypes=[("Text File", "*.txt")], defaultextension='*.txt')
    if save_file is None:
        print("File save has been cancelled")
        return False
    if type(data) == list:
        for line in data:
            if type(line) == list:
                for letter in line:
                    save_file.write(letter)
            else:
                save_file.write(line)
            save_file.write("\n")
    else:
        save_file.write(str(data))
    print("Data saved to: " + save_file.name)
    save_file.close()
    window.destroy()
    return True

def ask_question(title, message):
    window = t.Tk()
    window.withdraw()
    answer = messagebox.askyesno(title, message)
    window.destroy()
    return answer

def show_error(title, message):
    window = t.Tk()
    window.withdraw()
    messagebox.showerror(title, message)
    window.destroy()

def show_message(title, message):
    window = t.Tk()
    window.withdraw()
    messagebox.showinfo(title, message)
    window.destroy()

def show_warning(title, message):
    window = t.Tk()
    window.withdraw()
    messagebox.showwarning(title, message)
    window.destroy()

def keygen(message, key):
    if len(key) > len(message):
        new_key = key[:len(message)]
        return new_key
    else:
        key_pos = 0
        mes_pos = 0
        new_key = ""
        while mes_pos < len(message):
            if key_pos >= len(key):
                key_pos = 0
            if message[mes_pos] == " ":
                new_key = new_key + " "
                key_pos -= 1
            else:
                new_key = new_key + key[key_pos]
            key_pos += 1
            mes_pos += 1
        print("new_key is: " + new_key)
        return new_key
