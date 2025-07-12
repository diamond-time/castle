import sys
import os
usage = "Usage: python3 castle.py <height_1> <height_2>"
def main():
    init()
    
    
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
    print_castle(int(sys.argv[1]), int(sys.argv[2]))



def print_castle(h_castle_1, h_castle_2):
    print(f"Castle 1 height is {h_castle_1}, Castle 2 height is {h_castle_2}")
    #print(os.get_terminal_size())

def height_multiplier():
    multiplier=0.25
    return multiplier

main()