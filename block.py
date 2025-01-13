import tkinter as tk
from tkinter import filedialog, messagebox
import json

from python.Lib.dataclasses import asdict

import block_components
import dataTypes
from block_components import TextView, EditText
from util import h_getNextEmptyDictionary


class Block:
    # FIXED VARIABLES


    #"B_type" : {"id : 0", "block_id" : 1, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}}
    #"B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    #"B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

    def __init__(self):
        self.blocks = {}
        self.deletedPos = []
        self.editorObjects = {}
        #self.blocks[0] = {"B_type" : {"id" : 0, "block_id" : 0, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}},
        #                  "B_components" : {"id" : 0, "component" : None},
        #                  "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150}}
        print("done")

    def initBlock_add(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_editText = block_components.EditText()
        b_editText.setData(0, 10, 10, "Test", 1, "black", 10, 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 10, 30, "Test2", 1, "black", 10, 10)
        components = []
        components.insert(0, {"id": None, "component_id" : 1, "component": b_editText})
        components.insert(1, {"id": None, "component_id" : 1, "component": b_editText2})
        #components.__getitem__(1)
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
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
            "B_components" : components,
            "B_position" : {
                "x1": 50,
                "y1": 50,
                "x2": 150,
                "y2": 150}
        }
        return index

    def deleteBlock(self, block_id):
        self.blocks[block_id] = {}
        self.deletedPos[block_id].append(block_id)

    def findBlockIdFromCanvas(self, canvasId):
        stopAlg = 0
        for i in range(len(self.blocks)):
            for j in range(len(self.deletedPos)):
                if self.deletedPos.__getitem__(j) == canvasId:
                    print("was Deletes")
                    stopAlg = 1
                    break
                else:
                    stopAlg = 0
                    if self.blocks[i]["B_type"]["id"] == canvasId:
                        return i
                if stopAlg == 1:
                    return -1
        return -1

    def findBlockComponentIdFromCanvas(self, canvasId):
        stopAlg = 0
        for i in range(len(self.blocks)):
            for j in range(len(self.deletedPos)):
                if self.deletedPos.__getitem__(j) == canvasId:
                    print("was Deletes")
                    stopAlg = 1
                else:
                    stopAlg = 0
                    if self.blocks[i]["B_type"]["id"] == canvasId:
                        return i
                if stopAlg == 1:
                    return -1
        return -1




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