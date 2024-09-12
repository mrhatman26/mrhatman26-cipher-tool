import sys
import tkinter as t
from tkinter import filedialog as f
from input_handler import input_pause, input_binary_question
def v_table_generate():
    print("Vigenere Table Creation:\n")
    while True:
        try:
            alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            v_table = []
            key = str(input("Please enter a key: ")).upper()
            new_alphabet = alphabet
            x = 0
            for letter in key: #Add the key to the alphabet
                new_alphabet.insert(x, new_alphabet.pop(new_alphabet.index(letter)))
                x += 1
            shift_alphabet = new_alphabet
            i = 0
            while i < 26:
                v_table.append(shift_alphabet.copy())
                print("Current shift_alphabet copied to v_table")
                print("\nShift " + str(i + 1) + ":\nCurrent shift_alphabet: " + str(shift_alphabet))
                print("Moving " + str(shift_alphabet[0]) + " to end of list")
                shift_alphabet.append(shift_alphabet.pop(0))
                print("shift_alphabet is now: " + str(shift_alphabet))
                i += 1
            print("You vigenere table is the following: ")
            for line in v_table:
                i = 0
                for item in line:
                    if i == 25:
                        print(item)
                    else:
                        print(item + ", ", end="")
                    i += 1
            if input_binary_question("\nWould you like to save the generated vigenere table?: ") is True:
                window = t.Tk()
                window.withdraw()
                v_table_loc = t.filedialog.askdirectory()
                v_table_loc = v_table_loc + "/" + key + ".txt"
                window.destroy()
                v_table_file = open(v_table_loc, "w")
                for line in v_table:
                    for letter in line:
                        v_table_file.write(str(letter))
                    v_table_file.write("\n")
                v_table_file.close()
                print("\nVigenere table saved to " + v_table_loc + ".txt and loaded")
                input_pause()
            else:
                print("Vigenere table will not be saved, but will still be loaded")
                input_pause()
            return v_table
        except Exception as e:
            print("Error: " + str(e))
            print("Please try again")
            input_pause()

def v_table_load():
    print("Vigenere Table Loading:\n")
    window = t.Tk()
    window.withdraw()
    v_table = []
    try:
        v_table_file = t.filedialog.askopenfile(mode="r", filetypes=[("Text File", "*.txt")])
        for line in v_table_file:
            v_table_line = []
            for letter in line:
                print(letter, end="")
                if letter != "\n":
                    v_table_line.append(letter)
            v_table.append(v_table_line)
        v_table_file.close()
        for line in v_table:
            print(line)
            if len(line) != 26:
                raise Exception("v_table lines must all be 26 letters long.")
        if len(v_table) != 26:
            raise Exception("v_table must contain 26 lines.")
        print("Vigenere table loaded successfully")
        return v_table
    except Exception as e:
        print("Error: " + str(e))
        print("Vigenere table has NOT been loaded")
        input_pause()
        return None

def v_table_print(v_table):
    if v_table is not None:
        for line in v_table:
            print(line)
    else:
        print("No vigenere table has been loaded, please load a vigenere table and try again")
        input_pause()
    
