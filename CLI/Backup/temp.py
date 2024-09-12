from v_table import v_table_load
from misc import display_list_pos
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
                
my_string = "My message is really really bad"
v_table = v_table_load()
display_list_pos_multiline(v_table, 2, 4)
