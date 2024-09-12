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
