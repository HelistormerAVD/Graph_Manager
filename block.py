import tkinter as tk
from tkinter import filedialog, messagebox
import json

import block_components
import dataTypes
from block_components import TextView, EditText
from util import h_getNextEmptyDictionary, h_getVectorBetweenPoints


class Block:
    # FIXED VARIABLES

    # Block Höhe = 40 px

    #"B_type" : {"id : 0", "block_id" : 1, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}}
    #"B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    #"B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

    def __init__(self):
        self.blockHeight = 40
        self.blocks = {}
        self.deletedPos = []
        self.editorObjects = {}
        #self.blocks[0] = {"B_type" : {"id" : 0, "block_id" : 0, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}},
        #                  "B_components" : {"id" : 0, "component" : None},
        #                  "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150}}
        print("done")

    def initBlock_start(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text = block_components.TextView()
        b_text.setData(0, 10, 20, "Start", "black", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text})
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 1,
                "color": "green2",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes,
                    "outputBlockId": None},
                "func": {
                    "func_name": "NameOfFunction",
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 150,
                "y2": 90}
        }
        return index

    def initBlock_end(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text = block_components.TextView()
        b_text.setData(0, 10, 20, "End", "black", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text})
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 1,
                "color": "red",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes,
                    "outputBlockId": None},
                "func": {
                    "func_name": "NameOfFunction",
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 150,
                "y2": 90}
        }
        return index


    def initBlock_setVariable_add(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_editText = block_components.EditText()
        b_editText.setData(1, 10, 10, "Test", 10)
        b_text = block_components.TextView()
        b_text.setData(0, 10, 90, "+","black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 100, 10, "Test2", 10)
        components = []
        components.insert(0, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 1,
                "color": "green2",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "NameOfFunction",
                    "func_args" : None}
            },
            "B_components" : components,
            "B_position" : {
                "x1": 50,
                "y1": 50,
                "x2": 250,
                "y2": 90}
        }
        return index

    def initBlock_Integer_add(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Add Integer", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "+", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})
        components.insert(3, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 1,
                "color": "dodger blue",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "NameOfFunction",
                    "func_args" : None}
            },
            "B_components" : components,
            "B_position" : {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Integer_sub(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_editText = block_components.EditText()
        b_editText.setData(1, 10, 10, "Test", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 100, 10, "Test2", 10)
        components = []
        components.insert(0, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 1,
                "color": "green2",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "NameOfFunction",
                    "func_args" : None}
            },
            "B_components" : components,
            "B_position" : {
                "x1": 50,
                "y1": 50,
                "x2": 100,
                "y2": 100}
        }
        return index

    def deleteBlock(self, block_id):
        self.blocks[block_id] = {}
        self.deletedPos[block_id].append(block_id)

    def findBlockIdFromCanvas(self, canvasId):
        stopAlg = 0
        for i in range(self.blocks.__len__()):
            if self.deletedPos:
                for j in range(self.deletedPos.__len__()):
                    if self.deletedPos.__getitem__(j) == canvasId:
                        print("was Deletes")
                        stopAlg = 1
                    else:
                        stopAlg = 0
                        if self.blocks[i]["B_type"]["id"] == canvasId:
                            return i
                    if stopAlg == 1:
                        return -1
            else:
                if self.blocks[i]["B_type"]["id"] == canvasId:
                    return i
        return -1

    def setBlockPosition(self, block_id, x1, y1, x2, y2):
        self.blocks[block_id]["B_position"] = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

    def getBlockPosition(self, block_id):
        return self.blocks[block_id]["B_position"]

    def get_block_type(self, block_id):
        return self.blocks[block_id]["B_type"]

    def setBlockComponents(self, block_id, comp_id, comp):
        count = len(self.blocks[block_id]["B_components"])
        if comp_id < count:
            self.blocks[block_id]["B_components"][comp_id] = comp
            return 1
        else:
            return 0

    def moveBlock(self, block_id, x1, y1):
        oldPos = self.getBlockPosition(block_id)
        self.blocks[block_id]["B_position"] = {"x1" : x1, "y1" : y1, "x2" : x1 + (oldPos["x2"] - oldPos["x1"]), "y2" : y1 + (oldPos["y2"] - oldPos["y1"])}

    def moveBlockRelativ(self, block_id, x1, y1):
        oldPos = self.getBlockPosition(block_id)
        dx, dy = h_getVectorBetweenPoints(x1, y1, oldPos["x1"],oldPos["y1"])
        self.blocks[block_id]["B_position"] = {"x1" : (oldPos["x1"] + dx), "y1" : (oldPos["y1"] + dy), "x2" : (oldPos["x2"] + dx), "y2" : (oldPos["y2"] + dy)}


    def setAllBlockComponents(self, block_id, comp):
        self.blocks[block_id]["B_components"] = comp





if __name__ == "__main__":
    b_obj = Block()
    print(b_obj.blocks.__len__())
    b_obj.initBlock_Integer_add()