import tkinter as tk
from tkinter import filedialog, messagebox
import json

import block_components
import dataTypes
from block_components import TextView, EditText
from util import h_getNextEmptyDictionary


class Block:
    # FIXED VARIABLES
    b_editText = block_components.EditText()


    #"B_type" : {"id : 0", "block_id" : 1, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}}
    #"B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    #"B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

    def __init__(self):
        self.blocks = {}
        self.blocks[0] = {"B_type" : {"id" : 0, "block_id" : 0, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}},
                          "B_components" : {"id" : 0, "component" : TextView|EditText},
                          "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150}}
        print("done")

    def initBlock_add(self):
        index = h_getNextEmptyDictionary(self.blocks)
        self.blocks[index] = {
            "B_type" : {
                "id" : index,
                "block_id" : 1,
                "color": "green2",
                "connected" : False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "NameOfFunction"}
            },
            "B_components" : {
                "id" : 1,
                "component" : EditText},
            "B_position" : {
                "x1": 50,
                "y1": 50,
                "x2": 150,
                "y2": 150}
        }
        self.b_editText.setData(0, 10, 10, "Test", 1, "black", 50, 10)
        self.blocks[index]["B_components"][0] = {"id" : 0, "component" : self.b_editText}
        return index

    def setBlockPosition(self, block_id, x1, y1, x2, y2):
        self.blocks[block_id]["B_position"] = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

    def getBlockPosition(self, block_id):
        return self.blocks[block_id]["B_position"]

    def setBlockComponents(self, block_id, comp_id, comp):
        count = len(self.blocks[block_id]["B_components"])
        if comp_id < count:
            self.blocks[block_id]["B_components"][comp_id] = comp
            return 1
        else:
            return 0

    def setAllBlockComponents(self, block_id, comp):
        self.blocks[block_id]["B_components"] = comp




if __name__ == "__main__":
    b_obj = Block()
    print(b_obj.blocks.__len__())
    b_obj.initBlock_add()