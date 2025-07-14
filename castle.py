import sys
import os


usage = "Usage: python3 castle.py <height_1> <height_2>"

castle_top = [
    "          |>>>      ",
    "          |         ",
    "      _  _|_  _     ",
    "     |;|_|;|_|;|    ",
    r"     \\.    .  /    ",
    r"      \\:  .  /     "
]

castle_gap = "                    "

castle_middle = [
    "       ||:   |      ",
    "       ||:.  |      ",
    "       ||:  .|      ",
    "       ||:   |      ",
    "       ||: , |      ",
    "       ||:   |      ",
    "       ||: . |      "
]

castle_bottom = [
    "       ||: . |      ",
    "      _||_   |      ",
    "_ ---~    ~`---,    "
]
height_castle_1 = 0
height_castle_2 = 0
list_castle_1 = []
list_castle_2 = []
cycle = 0
def main():
    init()
    make_castle_1(list_castle_1)
    make_castle_2(list_castle_2)
    print_output(height_castle_1, height_castle_2)
    
    
def init():    
    #print(sys.argv)
    if len(sys.argv)!=3:
        print(f"Wrong number of arguments! {usage}")
        sys.exit(1)
    if isinstance(int(sys.argv[1]), int) == False or isinstance(int(sys.argv[2]), int) == False:
        #print(sys.argv[1])
        print(isinstance(int(sys.argv[1]), int))
        print(f"Heights must be integers. {usage}")
        sys.exit(1)
    if int(sys.argv[1]) > 100 or int(sys.argv[2]) > 100:
        print (f"Max height 100. {usage}")
        sys.exit(1)
    global height_castle_1
    global height_castle_2
    height_castle_1 = int(sys.argv[1])
    height_castle_2 = int(sys.argv[2])
    
def make_castle_1(castle_list):    
    if height_castle_1 < height_castle_2:    
        for i in range(0, height_castle_2 - height_castle_1):
            castle_list.append(castle_gap)
    add_top(castle_list)
    for i in range(0, height_castle_1):
        add_middle(castle_list)
    add_bottom(castle_list)
    pass

def make_castle_2(castle_list):
    if height_castle_2 < height_castle_1:    
        for i in range(0, height_castle_1 - height_castle_2):
            castle_list.append(castle_gap)
    add_top(castle_list)
    for i in range(0, height_castle_2):
        add_middle(castle_list)
    add_bottom(castle_list)    
    pass
    
def print_output(h_castle_1, h_castle_2):    
    for i in range(0, len(list_castle_1)):
        print(list_castle_1[i]+castle_gap+list_castle_2[i])
    print(f"Castle 1 height is {h_castle_1}, Castle 2 height is {h_castle_2}")
    #print(list_castle_1)
    #print(list_castle_2)
    pass

def height_multiplier():
    multiplier=1    
    #print(os.get_terminal_size()) 
    # will make it scale to height of the terminal using this and a multiplier
    return multiplier

def add_middle(castle_list):
    global cycle
    if cycle >= len(castle_middle):
        cycle = 0
    castle_list.append(castle_middle[cycle])
    cycle += 1

def add_top (castle_list):
    for i in castle_top:
        castle_list.append(i)
    pass

def add_bottom(castle_list):
    for i in castle_bottom:
        castle_list.append(i)

main()