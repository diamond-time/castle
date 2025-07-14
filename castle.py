import sys
import os
from sources import add_top


usage = "Usage: python3 castle.py <height_1> <height_2>"

castle_top = [
    "t1",
    "t2",
    "t3",
    "t4",
    "t5"
]

castle_middle = [
    "m1",
    "m2",
    "m3"
]

castle_bottom = [
    "b1",
    "b2",
    "b3",
    "b4",
    "b5"
]
height_castle_1 = 0
height_castle_2 = 0
list_castle_1 = []
list_castle_2 = []

def main():
    init()
    make_castle_1()
    make_castle_2()
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
    
def make_castle_1():
    
    pass

def make_castle_2():
    pass
    
def print_output(h_castle_1, h_castle_2):
    print(f"Castle 1 height is {h_castle_1}, Castle 2 height is {h_castle_2}")
    
    print(list_castle_1)
    print(list_castle_2)
    pass

def height_multiplier():
    multiplier=0.25
    #print(os.get_terminal_size()) 
    # will make it scale to height of the terminal using this and a multiplier
    return multiplier

def add_top (castle_list):
    for i in castle_top:
        castle_list.append(castle_top[i])


main()