from tkinter import mainloop
from unittest.main import MAIN_EXAMPLES
from pip import main
from utils.read_input import ReadInput

if __name__ == '__main__':
    # Read the input file
    filepath = "/Users/ambuj/Desktop/PycharmProject1/data/WhatsAppChat-Asha_part1.txt"
    conversations = ReadInput(filepath)
    print("DONE")