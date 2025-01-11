import tkinter as tk
from tkinter import filedialog, messagebox
import json

import block_components
import dataTypes
from block_components import TextView, EditText


class Block:
    # FIXED VARIABLES


    blocks = {"B_type" : {}, "B_components" : {}, "B_position" : {}}

    #"B_type" : {"id : 0", "block_id" : 1, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes}, "func" : {"func_name" : "NameOfFunction"}}
    #"B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    #"B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

    def __init__(self):
        self.blocks[0] = {"B_type" : {"id" : 0, "block_id" : 0, "color": "green", "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}},
                          "B_components" : {"id" : 0, "component" : TextView|EditText},
                          "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150}}

    def initBlock_add(self):
        length = self.blocks.__len__()

    def setBlockPosition(self, x1, y1, x2, y2):
        self.blocks[self]["B_position"] = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}



if __name__ == "__main__":
    Block()