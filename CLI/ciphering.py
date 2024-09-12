import tkinter as t
from tkinter import filedialog as f
from input_handler import input_pause, input_binary_question
from misc import zlen, display_list_pos, display_list_pos_multiline, load_file, save_file

def keygen(message, key):
    if len(key) > len(message):
        key = key[:len(message)]
    key_pos = 0
    mes_pos = 0
    new_key = ""
    print("Key length = " + str(zlen(key)))
    print("Message length = " + str(zlen(key)))
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
    return new_key

def process_cipher(message, new_key, v_table):
    cipher_text = ""
    letter_no = 0
    for letter in message.upper():
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
    return cipher_text

def process_decipher(message, new_key, v_table, show_list_pos):
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
            if show_list_pos is True:
                print("----------------------------------")
                display_list_pos_multiline(v_table, line_index, line_no)
            deciphered_text = deciphered_text + v_table[0][line_index]
        except:
            deciphered_text = deciphered_text + message[letter_no]
        letter_no += 1
    return deciphered_text

def cipher(v_table):
    print("Messaging Ciphering:\n")
    if v_table is None:
        print("No vigenere table is loaded. Please load a vigenere table and try again")
        input_pause()
        return
    if input_binary_question("Would you like to load a message from a text file?: ") is True:
        message_file = load_file()
        message = ""
        for line in message_file:
            message = message + line
            print(line)
        message_file.close()
        print("message = " + message)
    else:
        message = str(input("Please enter a message to cipher: ")).upper()
    key = str(input("Please enter a key to cipher the message: ")).upper()
    cipher_text = ""
    if "\n" in message:
        message = message.split("\n")
        cipher_text = []
        for line in message:
            new_key = keygen(line, key)
            cipher_text.append(process_cipher(line, new_key, v_table))
    else:
        new_key = keygen(message, key)
        cipher_text = process_cipher(message, new_key, v_table)
    print("Your ciphered text is: ")
    if type(cipher_text) == list:
        for item in cipher_text:
            print(item)
    else:
        print(cipher_text)
    input_pause()
    if input_binary_question("Would you like to save your ciphered text to a file?: ") is True:
        if save_file(cipher_text) is True:
            print("Ciphered text has been saved")
        else:
            print("Ciphered text has NOT been saved")
    else:
        print("Ciphere not saved")
    print("Ciphering complete")
    input_pause()
        
def decipher(v_table):
    print("Message deciphering:\n")
    if v_table is None:
        print("No vigenere table is loaded. Please load a vigenere table and try again")
        input_pause()
        return
    message = ""
    if input_binary_question("Would you like to load a message from a file?: ") is True:
        message_file = load_file()
        for line in message_file:
            message = message + line
            print(line)
        message_file.close()
    else:
        message = str(input("Please input your ciphered message: ")).upper()
    key = str(input("Please enter the key used to cipher the message: ")).upper()
    deciphered_text = ""
    if "\n" in message:
        message = message.split("\n")
        deciphered_text = []
        for line in message:
            new_key = keygen(line, key)
            deciphered_text.append(process_decipher(line, new_key, v_table, False))
    else:
        new_key = keygen(message, key)
        deciphered_text = process_decipher(message, new_key, v_table, True)
    print("\nYour deciphered text is: ")
    if type(deciphered_text) == list:
        for item in deciphered_text:
            print(item)
    else:
        print(deciphered_text)
    input_pause()
    if input_binary_question("Would you like to save the deciphered text to a file?: ") is True:
        if save_file(deciphered_text) is True:
            print("Deciphered text has been saved")
        else:
            print("Deciphered text has NOT been saved")
    else:
        print("Decipher not saved")
    print("Deciphering complete")
    input_pause()
