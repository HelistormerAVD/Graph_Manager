import tkinter as tk
from tkinter import filedialog, messagebox
import json

import block_components
import dataTypes
from block_components import TextView, EditText
from dataTypes import BDInteger
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
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 0,
                "block_tag": "start",
                "color": "green2",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDInteger(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDInteger(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_start",
                    "func_args_list": args,
                    "isPassThrough": False,
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
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 1,
                "block_tag": "end",
                "color": "red",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDInteger(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDInteger(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "NameOfFunction",
                    "func_args_list": args,
                    "isPassThrough": False,
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
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Set Variable", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "to", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})
        components.insert(3, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 2,
                "block_tag": "set_variable",
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
                    "func_args_list": args,
                    "isPassThrough": False,
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

    #--------------------------Wichtig für Blockerstellung!-------------------------
    #   Beispiel:
    #   b_textView = block_components.TextView()
    #   b_textView.setData(0, 10, 20, "Add Integer", "black", 23)
    #   -------------------
    #   setData(<component_id> 0, 10, ...) Die component_id muss dem Klassentyp der Komponente Entsprechen:
    #   Hierbei ist 0 = TextView und 1 = EditText
    #   Zudem ist bei component_id = 0 der Wert y1 = 20 und bei component_id = 1 der Wert y1 = 10
    #
    #   setData(..., "black", <width> 23) Die 23 sind die Anzahl der Character die im <text> angegeben sind.
    #   sollte am besten gleich lang sein, damit es keine überlappungen gibt.
    #   -----
    #
    #   components = []
    #   components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
    #   components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
    #   ------------------
    #   Der Index bei "components.insert(<index> 0,...)" darf nicht zweimal vorkommen.
    #   Am besten in der richtigen Reihenfolge einfügen, wie die Komponenten von link nach rechts angeornet sind.
    #   -----
    #
    #   in self.blocks[index] = {...} müssen folgende Einträge beachtet werden:
    #
    #   "block_id" : "<eindeutige Id des Blocks>"
    #   "color" : "<farbe des Blocks passend aus usedColors.py zu entnehmen>"
    #   "block_tag": "<datentyp kleingeschrieben>_<funktion des Blocks>" (Beispiel: "integer_add", "integer_sub", "float_add")
    #   "func_name" : "f_<datentyp kleingeschrieben kurzform>_<funktion des Blocks>" (Beispiel: "f_int_add", "f_int_sub", "f_float_add")
    #   "input_t" : dataTypes.<datenTyp> (Beispiel: "input_t" : dataTypes.BDInteger)
    #   "input_id": <id passend zum <datenTyp> in "input_t"> (Beispiel: "input_id" : 0) -> Tabelle mit Ids in dataTypes.py
    #   "output_t" : dataTypes.<datenTyp> (Beispiel: "output_t" : dataTypes.BDInteger)
    #   "output_id": <id passend zum <datenTyp> in "output_t"> (Beispiel: "output_id" : 0) -> Tabelle mit Ids in dataTypes.py
    #   -----
    #
    #   Der Rest ist entweder None oder False
    #
    #   Neu: args = []
    #   ist eine Liste, die die component_ids von "components = []" besitzt.
    #   Neu: "func_args_list": args -> beinhaltet args Liste
    #   Neu: "isPassThrough": True -> Flag, welches standardgemäß True ist, sofern eine Funktion den wert Weitergeben soll.


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
        args = [1,3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 3,
                "block_tag": "integer_add",
                "color": "dodger blue",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDInteger(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_int_add",
                    "func_args_list": args,
                    "isPassThrough": True,
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
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Sub Integer", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "-", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 4,
                "block_tag": "integer_sub",
                "color": "dodger blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDInteger,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDInteger,
                    "outputBlockId": None},
                "func": {
                    "func_name": "NameOfFunction",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Integer_div(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Div Integer", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "/", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})
        components.insert(3, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 5,
                "block_tag": "integer_div",
                "color": "dodger blue",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDInteger,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "NameOfFunction",
                    "func_args_list": args,
                    "isPassThrough": False,
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

    def initBlock_Integer_mult(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Mult Integer", "black", 23)
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
        args = []
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 6,
                "block_tag": "integer_mult",
                "color": "dodger blue",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDInteger,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "NameOfFunction",
                    "func_args_list": args,
                    "isPassThrough": False,
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

    #--------------------------------------------------------------------------------------------------------------------------------
    #
    #                       Funktionen für Blöcke

 #flaot / double
    def initBlock_Float_add(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Add Float", "black", 23)
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
        args = []
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 7,
                "block_tag": "float_add",
                "color": "blue",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 1,
                    "input_t" : dataTypes.BDFloat,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 1,
                    "output_t" : dataTypes.BDFloat,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_float_add",
                    "func_args_list": args,
                    "isPassThrough": False,
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

    def initBlock_Float_sub(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Sub Float", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "-", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 8,
                "block_tag": "float_sub",
                "color": "blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 1,
                    "input_t": dataTypes.BDFloat,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_float_sub",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Float_div(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Div Float", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "/", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 9,
                "block_tag": "float_div",
                "color": "blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 1,
                    "input_t": dataTypes.BDFloat,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_float_div",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Float_mult(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Mult Float", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "+", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 10,
                "block_tag": "integer_mult",
                "color": "blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 1,
                    "input_t": dataTypes.BDFloat,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_float_mult",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index



# string
    def initBlock_Str_concat(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Str_Concat", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, " ", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 11,
                "block_tag": "str_concat",
                "color": "saddle brown",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_concat",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Str_subDiv(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "String subDiv", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, " ", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 12,
                "block_tag": "str_subDiv",
                "color": "saddle brown",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_subDiv",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Str_trim(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Str_trim", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, " ", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 13,
                "block_tag": "str_trim",
                "color": "saddle brown",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_trim",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    def initBlock_Str_split(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Str_split", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, " ", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 14,
                "block_tag": "str_split",
                "color": "saddle brown",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_split",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index
    def initBlock_Str_find(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Str_find", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, " ", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 15,
                "block_tag": "str_find",
                "color": "saddle brown",
                "outline": "light gray",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_find",
                    "func_args_list": args,
                    "isPassThrough": False,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 50,
                "y1": 50,
                "x2": 350,
                "y2": 90}
        }
        return index

    #
    #--------------------------------------------------------------------------------------------------------------------------------

    def f_start(self):
        print("no Operation")

    def f_int_add(self, a, b):

        print("!!Function!!")

    def f_int_sub(self):
        print("Function")

    def f_int_div(self):
        print("Function")

    def f_int_div_to_int(self):
        print("Function")

    def f_int_mult(self):
        print("Function")






if __name__ == "__main__":
    b_obj = Block()
    print(b_obj.blocks.__len__())
    b_obj.initBlock_Integer_add()