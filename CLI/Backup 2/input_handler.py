def input_pause():
    input("(Press ENTER to continue)")

def input_binary_question(question):
    while True:
        if question == "" or question == None:
            user_input = str(input("Yes (Y) / No (N)?: ")).upper()
        else:
            user_input = str(input(question)).upper()
        if user_input in "Y" "YES":
            return True
        elif user_input in "N" "NO":
            return False
        elif user_input == "":
            print("Please enter Y or N.")
            input_pause()
            print("\n")
        else:
            print("Please enter Y or N.")
            input_pause()
            print("\n")
