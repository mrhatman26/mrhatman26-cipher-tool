import sys
from v_table import v_table_generate, v_table_load, v_table_print
from ciphering import cipher, decipher
from input_handler import input_pause
v_table = None
while True:
    print("Main Menu:\n")
    if v_table is not None:
        print("Vigenere table loaded!\n")
        input_pause()
    option = str(input("What would you like to do? (Type 'help' for options): ")).upper()
    if option == "HELP" or option == "H":
        print("Options:\n'help': See this screen.")
        print("-'g' / 'generate': Generate a vigenere table.")
        print("-'l' / 'load': Load a vigenere table.")
        print("-'p' / 'print': Displays the loaded vigenere table if it exists")
        print("-'c' / 'cipher': Cipher a message using the loaded vigenere table")
        print("-'d' / 'decipher': Decipher a message using the loaded vigenere table")
        print("-'exit': Exit the program")
        input_pause()
        print("\n")
    elif option == "EXIT" or option == "E":
        print("Bye, bye!")
        input_pause()
        sys.exit()
    elif option == "GENERATE" or option == "G":
        v_table = v_table_generate()
    elif option == "LOAD" or option == "L":
        v_table = v_table_load()
    elif option == "PRINT" or option == "P":
        v_table_print(v_table)
    elif option == "CIPHER" or option == "C":
        cipher(v_table)
    elif option == "DECIPHER" or option == "D":
        decipher(v_table)
    else:
        print(option + " is not a valid option.\nPlease try again")
        input_pause()
        
