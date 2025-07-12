import sys

def main():
    print("Usage: python3 castle.py <height_1> <height_2>")
    if len(sys.argv)!=3:
        sys.exit(1)
    castle(sys.argv[1], sys.argv[2])