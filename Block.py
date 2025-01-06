import tkinter as tk
from tkinter import filedialog, messagebox
import json


class Block:
    # FIXED VARIABLES
    BLOCK_ID = 0
    BLOCK_POS_X = 0
    BLOCK_POS_Y = 0
    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 20
    canvas = tk.Canvas()

    # LOKAL VARIABLES
    B_layout = {}
    B_color = None
    B_inputTypes = {}
    B_outputTypes = {}

    def __init__(self, tkCanvas):
        self.BLOCK_ID = 0
        self.initBlock_add(tkCanvas)

    def initBlock_add(self, tkCanvas):
        self.BLOCK_ID = 1
        self.BLOCK_POS_X = 10
        self.BLOCK_POS_Y = 10
        self.BLOCK_WIDTH = 20
        self.BLOCK_HEIGHT = 20
        self.canvas = tkCanvas


if __name__ == "__main__":
    Block()
