import tkinter as t
from tkinter import filedialog as f
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
            save_file.write(line)
            save_file.write("\n")
    else:
        save_file.write(data)
    print("Data saved to: " + save_file.name)
    save_file.close()
    return True
