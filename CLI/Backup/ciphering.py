import tkinter as t
from tkinter import filedialog as f
from input_handler import input_pause, input_binary_question
from misc import zlen, display_list_pos, display_list_pos_multiline
def cipher(v_table):
    print("Messaging Ciphering:\n")
    if v_table is None:
        print("No vigenere table is loaded. Please load a vigenere table and try again")
        input_pause()
        return
    if input_binary_question("Would you like to load a message from a text file?: ") is True:
        window = t.Tk()
        window.withdraw()
        message_file = t.filedialog.askopenfile(mode="r", filetypes=[("Text File", "*.txt")])
        message = ""
        for line in message_file:
            message = message + line
            print(line)
        message_file.close()
        print("message = " + message)
    else:
        message = str(input("Please enter a message to cipher: ")).upper()
    key = str(input("Please enter a key to cipher the message: ")).upper()
    if len(key) > len(message):
        key = key[:len(message)]
    key_pos = 0
    mes_pos = 0
    new_key = ""
    print("Key length = " + str(zlen(key)))
    while mes_pos < len(message):
        print("mess_pos = " + str(mes_pos) + "\nkey_pos = " + str(key_pos))
        display_list_pos(message, mes_pos, True)
        if key_pos >= len(key):
            key_pos = 0
        if message[mes_pos] == " ":
            new_key = new_key + " "
            key_pos -= 1
        else:
            new_key = new_key + key[key_pos]
        key_pos += 1
        mes_pos += 1
    print(new_key + " (Length is " + str(len(new_key)) + ")")
    print(message + " (Length is " + str(len(message)) + ")")
    input_pause()
    cipher_text = ""
    letter_no = 0
    for letter in message:
        #Find the message's current letter at the start of each line.
        line_no = 0
        for line in v_table:
            if line[0] == letter:
                break
            line_no += 1
        #Find the index of the current key letter
        try:
            line_index = v_table[0].index(new_key[letter_no])
            cipher_text = cipher_text + v_table[line_no][line_index]
        except:
            cipher_text = cipher_text + letter
        letter_no += 1
    print("\nYour ciphered text is: " + cipher_text)
    input_pause()
    if input_binary_question("Would you like to save this to a file?: ") is True:
        window = t.Tk()
        window.withdraw()
        save_file = t.filedialog.asksaveasfile(filetypes=[("Text File", "*.txt")], defaultextension='*.txt')
        if save_file is not None:
            save_file.write(cipher_text)
            save_file.close()
            print("Ciphered text saved")
        else:
            print("Save cancelled")
    else:
        print("Cipher not saved")
        
def decipher(v_table):
    print("Message deciphering:\n")
    if v_table is None:
        print("No vigenere table is loaded. Please load a vigenere table and try again")
        input_pause()
        return
    message = ""
    if input_binary_question("Would you like to load a message from a file?: ") is True:
        window = t.Tk()
        window.withdraw()
        message_file = t.filedialog.askopenfile(mode="r", filetypes=[("Text File", "*.txt")])
        for line in message_file:
            message = message + line
            print(line)
        message_file.close()
    else:
        message = str(input("Please input your ciphered message: ")).upper()
    key = str(input("Please enter the key used to cipher the message: ")).upper()
    '''Woah'''
    if len(key) > len(message):
        key = key[:len(message)]
    key_pos = 0
    mes_pos = 0
    new_key = ""
    print("Key length = " + str(zlen(key)))
    while mes_pos < len(message):
        print("mess_pos = " + str(mes_pos) + "\nkey_pos = " + str(key_pos))
        display_list_pos(message, mes_pos, True)
        if key_pos >= len(key):
            key_pos = 0
        if message[mes_pos] == " ":
            new_key = new_key + " "
            key_pos -= 1
        else:
            new_key = new_key + key[key_pos]
        key_pos += 1
        mes_pos += 1
    print("new_key = " + new_key)
    print("message = " + message)
    input_pause()
    '''Huh'''
    deciphered_text = ""
    letter_no = 0
    for key_letter in new_key:
        print("key_letter = " + key_letter)
        line_no = 0
        for line in v_table:
            if line[0] == key_letter:
                break
            line_no += 1
        try:
            line_index = v_table[line_no].index(message[letter_no])
            print("----------------------------------")
            display_list_pos_multiline(v_table, line_index, line_no)
            deciphered_text = deciphered_text + v_table[0][line_index]
        except:
            deciphered_text = deciphered_text + message[letter_no]
        letter_no += 1
    print("\nYour deciphered text is: " + deciphered_text)
    input_pause()
