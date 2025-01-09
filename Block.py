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

    blocks = {"B_type" : {}, "B_components" : {}, "B_position" : {}}

    #"B_type" : {"id : 0", "block_id" : 1, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes}, "func" : {"func_name" : "NameOfFunction"}}
    #"B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    #"B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

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
