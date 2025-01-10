import tkinter as tk
from tkinter import filedialog, messagebox
import json

import BlockComponents
import dataTypes


class Block:
    # FIXED VARIABLES


    blocks = {"B_type" : {}, "B_components" : {}, "B_position" : {}}

    #"B_type" : {"id : 0", "block_id" : 1, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes}, "func" : {"func_name" : "NameOfFunction"}}
    #"B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    #"B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

    def __init__(self):
        self.blocks[0] = {"B_type" : {"id" : 0, "block_id" : 1, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}},
                          "B_components" : {"id" : 0, "component" : BlockComponents},
                          "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}}

    def initBlock_add(self):
        length = self.blocks.__len__()



if __name__ == "__main__":
    Block()
