import tkinter as t
from tkinter.ttk import *
from class_main_menu import MainMenu
from class_cipher import CipherWindow
from class_decipher import DecipherWindow
from class_v_table import VTableCreation, VTableLoading
from misc import *
if __name__ == "__main__":
    v_table = None
    p_name = "MrHatman26's Cipher Tool"
    while True:
        option = -1
        option = MainMenu(res_spec(880, 600), p_name + " - Main Menu", False, False, v_table).pack_and_run()
        print("option = " + str(option))
        if option == 0:
            v_table = VTableCreation(res_spec(340, 500), p_name + " - Vigenere Table Generation", False, False).pack_and_run()
            if v_table is None:
                show_warning("No Vigenere Table", "Warning: No vigenere table was loaded")
            else:
                show_message("Load Successful", "Vigenere table loaded successfully")
        if option == 1:
            v_table = VTableLoading()
            if v_table is None:
                show_warning("No Vigenere Table", "Warning: No vigenere table was loaded")
            else:
                show_message("Load Successful", "Vigenere table loaded successfully")
        if option == 2:
            if v_table is None:
                show_error("No Table Error", "No vigenere table has been loaded, please try again.")
            else:
                CipherWindow(res_spec(600, 160), p_name + " - Cipher Menu", False, False, v_table).pack_and_run()
        if option == 3:
            if v_table is None:
                show_error("No Table Error", "No vigenere table has been loaded, please try again.")
            else:
                DecipherWindow(res_spec(600, 160), p_name + " - Decipher Menu", False, False, v_table).pack_and_run()
print("Bye, bye! :)")
