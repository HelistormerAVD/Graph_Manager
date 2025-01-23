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
        self.blocks = {} # muss in Json gespeichert und geladen werden (in einer Datei)
        self.deletedPos = [] # muss in Json gespeichert und geladen werden (in einer Datei)
        self.editorObjects = {} # nicht benötigt.
        self.exec_obj = [] # TEMP muss noch auf 0 gesetzt werden beim Laden
        self.funcList = [] # TEMP muss noch auf 0 gesetzt werden beim Laden
        self.loopList = [] # TEMP muss noch auf 0 gesetzt werden beim Laden
        self.tempEntry = None
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


    def initBlock_setVariable(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Set Variable", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "$VariableName", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "to", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})
        components.insert(3, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 2,
                "block_tag": "set_variable",
                "color": "orange red",
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
                    "func_name" : "f_set_variable",
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
                    "input_t": dataTypes.BDInteger(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDInteger(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_int_sub",
                    "func_args_list": args,
                    "isPassThrough": True,  # war vorher false?
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
                    "input_t" : dataTypes.BDInteger(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_int_div",
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
                    "input_t" : dataTypes.BDInteger(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_int_mult",
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



    def deleteBlock(self, block_id):
        self.blocks[block_id] = {}
        self.deletedPos[block_id].append(block_id)

    def findBlockIdFromCanvas(self, canvasId):
        stopAlg = 0
        for i in range(self.blocks.__len__()):
            if self.deletedPos:
                for j in self.deletedPos:
                    if j == i:
                        print("was Deletes")
                        stopAlg = 1
                    else:
                        print(f"J = {j}, canvasId = {canvasId}")
                        print(self.blocks.__len__())
                        print(i)
                        print(self.blocks)
                        print(self.blocks[0])
                        print(self.deletedPos)
                        print(f"block: {self.blocks[i]} Deleted Pos: {self.deletedPos}")
                        stopAlg = 0
                        if self.blocks[i]["B_type"]["id"] == canvasId:
                            return i
                    if stopAlg == 1:
                        print("skipped")
            else:
                if self.blocks[i]["B_type"]["id"] == canvasId:
                    return i
        return None

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

    #float / double
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
                "color": "royal blue",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 1,
                    "input_t" : dataTypes.BDFloat(0.0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 1,
                    "output_t" : dataTypes.BDFloat(0.0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_float_add",
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
                "color": "royal blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 1,
                    "input_t": dataTypes.BDFloat(0.0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat(0.0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_float_sub",
                    "func_args_list": args,
                    "isPassThrough": True,
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
                "color": "royal blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 1,
                    "input_t": dataTypes.BDFloat(0.0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat(0.0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_float_div",
                    "func_args_list": args,
                    "isPassThrough": True,
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
        b_textView2.setData(0, 175, 20, "*", "black", 10)
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
                "color": "royal blue",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 1,
                    "input_t": dataTypes.BDFloat(0.0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat(0.0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_float_mult",
                    "func_args_list": args,
                    "isPassThrough": True,
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
        b_editText.setData(1, 100, 10, "first", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "with", "black", 23)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 225, 10, "secund", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = [1,3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 11,
                "block_tag": "str_concat",
                "color": "deep pink",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString(""),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString(""),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_concat",
                    "func_args_list": args,
                    "isPassThrough": True,
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
##????
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
                "color": "deep pink",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString(""),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString(""),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_subDiv",
                    "func_args_list": args,
                    "isPassThrough": True,
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
        b_editText.setData(1, 100, 10, "text", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(1, {"id": None, "component_id": 0, "entry": None, "component": b_textView})

        args = [0]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 13,
                "block_tag": "str_trim",
                "color": "deep pink",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString(""),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString(""),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_trim",
                    "func_args_list": args,
                    "isPassThrough": True,
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
        b_editText.setData(1, 100, 10, "zeichen", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "in", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "text", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = [1,3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 14,
                "block_tag": "str_split",
                "color": "deep pink",
                "outline": "black",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString(""),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString(""),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_split",
                    "func_args_list": args,
                    "isPassThrough": True,
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
        b_textView.setData(0, 10, 20, "find Str", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "String", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "in", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "text", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = [1,3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 15,
                "block_tag": "str_find",
                "color": "deep pink",
                "outline": "light gray",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 2,
                    "input_t": dataTypes.BDString(""),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString(""),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_str_find",
                    "func_args_list": args,
                    "isPassThrough": True,
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


    def initBlock_Function(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Function", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "f_nameOfFunction", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        args = [1]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 16,
                "block_tag": "funcBlock",
                "color": "teal",
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
                    "func_name" : "f_nop",
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

    def initBlock_Goto(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Goto", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "f_nameOfFunction", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        args = [1,3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 17,
                "block_tag": "goto",
                "color": "teal",
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
                    "func_name" : "f_nop",
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


    def initBlock_FunctionReturn(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "return to", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "f_nameOfFunction", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        args = [1,3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 18,
                "block_tag": "funcReturn",
                "color": "teal",
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
                    "func_name" : "f_nop",
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

    def initBlock_If(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "if", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        args = [1]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 19,
                "block_tag": "if",
                "color": "orange",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDInteger(0),  #01 true false
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_nop",
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

    def initBlock_WhileLoop_end(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Loop End", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "l_test", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        args = [1]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 20,
                "block_tag": "whileLoopEnd",
                "color": "orange",
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
                    "func_name" : "f_nop",
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

    def initBlock_WhileLoop(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "While-Loop", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "l_test", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "1 ==", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 21,
                "block_tag": "whileLoop",
                "color": "orange",
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
                    "func_name" : "f_nop",
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

    # !!! BDList nicht vorhanden
    def initBlock_List_Insert(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Insert in list", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "Wert", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "in", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "Liste", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})
        components.insert(3, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        args = [1,3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 22,
                "block_tag": "list_insert",
                "color": "mediumpurple",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDList(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDList(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_list_insert",
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


    def initBlock_List_get(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "get List", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "liste", 10)
        components = []
        components.insert(0, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(1, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})

        args = [0]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 23,
                "block_tag": "list_get",
                "color": "mediumpurple",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDList(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDList(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_list_get",
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

    def initBlock_List_delete(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "delete List", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "liste", 10)

        components = []

        components.insert(0, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(1, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})

        args = [0]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 24,
                "block_tag": "list_delete",
                "color": "mediumpurple",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDList(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDList(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_list_delete",
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

    def initBlock_List_sort(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "sort List", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "Liste", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "mit", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "sort_art", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry" : None, "component": b_textView})
        components.insert(3, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText2})
        args = [1,3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 25,
                "block_tag": "list_sort",
                "color": "mediumpurple",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDList(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDList(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_list_sort",
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




    def initBlock_set_Graph(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Set Graph  x:", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "x-werte", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "y:", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "y-werte", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 26,
                "block_tag": "set_graph",
                "color": "khaki2",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDInteger(0),
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 4,
                    "output_t" : dataTypes.BDGraph(),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_set_graph",
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

# def modify_graph(self, x, y, x_label, y_label, title, grid, label):

    def initBlock_modify_Graph(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "modify Graph", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 120, 10, "graph", 10)

        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 200, 20, "x:", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 250, 10, "wert", 10)

        b_textView3 = block_components.TextView()
        b_textView3.setData(0, 325, 20, "y:", "black", 10)
        b_editText3 = block_components.EditText()
        b_editText3.setData(1, 375, 10, "wert", 10)


        b_textView4 = block_components.TextView()
        b_textView4.setData(0, 200, 40, "x-label", "black", 10)
        b_editText4 = block_components.EditText()
        b_editText4.setData(1, 250, 30, "label", 10)

        b_textView5 = block_components.TextView()
        b_textView5.setData(0, 325, 40, "y-label", "black", 10)
        b_editText5 = block_components.EditText()
        b_editText5.setData(1, 375, 30, "label", 10)


        b_textView6 = block_components.TextView()
        b_textView6.setData(0, 200, 60, "title", "black", 10)
        b_editText6 = block_components.EditText()
        b_editText6.setData(1, 250, 50, "titel", 10)


        b_textView7 = block_components.TextView()
        b_textView7.setData(0, 325, 60, "grid", "black", 10)
        b_editText7 = block_components.EditText()
        b_editText7.setData(1, 375, 50, "grid", 10)

        b_textView8 = block_components.TextView()
        b_textView8.setData(0, 450, 60, "label", "black", 10)
        b_editText8 = block_components.EditText()
        b_editText8.setData(1, 500, 50, "label", 10)


        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})
        components.insert(4, {"id": None, "component_id": 0, "entry": None, "component": b_textView3})
        components.insert(5, {"id": None, "component_id": 1, "entry": None, "component": b_editText3})
        components.insert(6, {"id": None, "component_id": 0, "entry": None, "component": b_textView4})
        components.insert(7, {"id": None, "component_id": 1, "entry": None, "component": b_editText4})
        components.insert(8, {"id": None, "component_id": 0, "entry": None, "component": b_textView5})
        components.insert(9, {"id": None, "component_id": 1, "entry": None, "component": b_editText5})
        components.insert(10, {"id": None, "component_id": 0, "entry": None, "component": b_textView6})
        components.insert(11, {"id": None, "component_id": 1, "entry": None, "component": b_editText6})
        components.insert(12, {"id": None, "component_id": 0, "entry": None, "component": b_textView7})
        components.insert(13, {"id": None, "component_id": 1, "entry": None, "component": b_editText7})
        components.insert(14, {"id": None, "component_id": 0, "entry": None, "component": b_textView8})
        components.insert(15, {"id": None, "component_id": 1, "entry": None, "component": b_editText8})




        args = [1,3,5,7,9,11,13,15]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 27,
                "block_tag": " modi_graph",
                "color": "khaki2",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDGraph(),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDGraph(),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_modi_graph",
                    "func_args_list": args,
                    "isPassThrough": True,
                    "func_args": None}
            },
            "B_components": components,
            "B_position": {
                "x1": 10,
                "y1": 50,
                "x2": 600,
                "y2": 150}
        }
        return index

    def initBlock_get_Graph(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Get Graph", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "graph", 10)

        components = []
        components.insert(0, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(1, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        args = [0]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 28,
                "block_tag": "get_graph",
                "color": "khaki2",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 4,
                    "input_t" : dataTypes.BDGraph,
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 4,
                    "output_t" : dataTypes.BDGraph,
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_get_graph",
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

    def initBlock_nop(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text = block_components.TextView()
        b_text.setData(0, 10, 20, "NOP", "black", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 29,
                "block_tag": "nop",
                "color": "gray50",
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
                    "func_name": "f_nop",
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

    def initBlock_loadFileInList(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "Load File", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "<path>", 10)
        b_textView2 = block_components.TextView()
        b_textView2.setData(0, 175, 20, "in List", "black", 10)
        b_editText2 = block_components.EditText()
        b_editText2.setData(1, 200, 10, "<ListVar>", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_editText})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_editText2})

        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 30,
                "block_tag": "loadFileInList",
                "color": "salmon4",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDInteger(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDGraph,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_nop",
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

    def initBlock_Print(self):
        index = h_getNextEmptyDictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_textView = block_components.TextView()
        b_textView.setData(0, 10, 20, "if", "black", 23)
        b_editText = block_components.EditText()
        b_editText.setData(1, 100, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_textView})
        components.insert(1, {"id": None, "component_id" : 1, "entry" : None, "component": b_editText})
        args = [1]
        self.blocks[index] = {
            "B_type" : {
                "id" : None,
                "block_id" : 31,
                "block_tag": "print",
                "color": "gray50",
                "connected" : False,
                "inLoop": False,
                "block_inputTypes" : {
                    "input_id" : 0,
                    "input_t" : dataTypes.BDInteger(0),  #01 true false
                    "inputBlockId" : None},
                "block_outputTypes" : {
                    "output_id" : 0,
                    "output_t" : dataTypes.BDInteger(0),
                    "outputBlockId" : None},
                "func" : {
                    "func_name" : "f_nop",
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

    #
    #--------------------------------------------------------------------------------------------------------------------------------

    # wenn es zu fehlern mit der Ausführung kommt, kann es sein das Methoden als Static deklariert sein müssen oder auch nicht.
    def f_start(self):
        print("no Operation")

    def f_nop(self, *args):
        print("no Operation")

    def f_set_variable(self, g_var, a, b):
        if isinstance(a, dataTypes.BDString):
            g_var.insert_value(a.__getstate__(), b)
            return b
        else:
            print("Variable muss ein String mit $<name> sein!")

    """ BDInteger Funktions-Handler """
    def f_int_add(self, a, b):
        if self.is_type_bd_int(a, b):
            a.add(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_int_sub(self, a, b):
        if self.is_type_bd_int(a, b):
            a.subtract(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_int_mult(self, a, b):
        if self.is_type_bd_int(a, b):
            a.multiply(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    # BDFloat divide Funktion???
    def f_int_div(self, a, b):
        if self.is_type_bd_int(a, b):
            a.divide(b.__getstate__())
            print(a.__getstate__())
            c = dataTypes.BDFloat(a)
            return c
        else:
            print("Falscher Datentyp!")

    def f_int_pow(self, a, b):
        if self.is_type_bd_int(a, b):
            a.BDInteger.pow(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_int_mod(self, a, b):
        if self.is_type_bd_int(a, b):
            a.BDInteger.modulo(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_int_div_to_int(self, a, b):
        if self.is_type_bd_int(a, b):
            a.divide(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    """ BDFloat Funktions-Handler """
    def f_float_add(self, a, b):
        if self.is_type_bd_float(a, b):
            a.BDFloat.add(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_float_sub(self, a, b):
        if self.is_type_bd_float(a, b):
            a.BDFloat.subtract(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_float_mul(self, a, b):
        if self.is_type_bd_float(a, b):
            a.BDFloat.multiply(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_float_div(self, a, b):
        if self.is_type_bd_float(a, b):
            a.BDFloat.divide(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_float_pow(self, a, b):
        if self.is_type_bd_int(a, b):
            a.BDFloat.pow(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    """ BDString Funktions-Handler """
    def f_str_concat(self, s1, s2):
        if self.is_type_bd_string(s1, s2):
            s1.BDString.concat(s2)
            print(s1.__getstate__())
            return s1
        else:
            print("Falscher Datentyp!")

    def f_str_find(self, s1, s2):
        if self.is_type_bd_string(s1, s2):
            s1.BDString.find(s2)
            print(s1.__getstate__())
            return s1
        else:
            print("Falscher Datentyp!")

    def f_str_replace(self, s, s1, s2):
        if isinstance(s, dataTypes.BDString) and self.is_type_bd_string(s1, s2):
            s1.BDString.replace(s1, s2)
            print(s1.__getstate__())
            return s1
        else:
            print("Falscher Datentyp!")

    def f_str_split(self, s1, s2):
        if self.is_type_bd_string(s1, s2):
            s1.BDString.find(s2)
            print(s1.__getstate__())
            return s1
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_str_trim(s1):
        if isinstance(s1, dataTypes.BDString):
            s1.trim()
            print(s1.__getstate__())
            return s1
        else:
            print("Falscher Datentyp!")

    """ BDList Funktions-Handler """
    def f_list_init(self, data):
        if isinstance(data, list) or isinstance(data, dataTypes.BDList):
            dataTypes.BDList(self.get_list_value(data))
            print(data.__getstate__())
            return data
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_append(bd_list, elem):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.append(elem)
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_clear(bd_list):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.clear()
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_copy(bd_list):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.copy()
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_count(bd_list, elem):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.count(elem)
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    def f_list_extend(self, bd_list, data):
        if isinstance(bd_list, dataTypes.BDList) and self.is_type_list(data):
            bd_list.extend(self.get_list_value(data))
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_index(bd_list, elem):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.index(elem)
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    # TODO: pos vom Typ BDInteger oder int???
    def f_list_insert(self, bd_list, pos, elem):
        if isinstance(bd_list, dataTypes.BDList) and self.is_type_int(pos):
            bd_list.insert(
                self.get_int_value(pos),
                elem
            )
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    def f_list_pop(self, bd_list, pos):
        if isinstance(bd_list, dataTypes.BDList) and self.is_type_int(pos):
            bd_list.pop(self.get_int_value(pos))
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_remove(bd_list, elem):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.remove(elem)
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_reverse(bd_list):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.reverse()
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_list_sort(bd_list):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.sort()
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    def f_list_set(self, data):
        self.f_list_init(data)

    @staticmethod
    def f_list_get(bd_list):
        if isinstance(bd_list, dataTypes.BDList):
            bd_list.get_list()
            print(bd_list.__getstate__())
            return bd_list
        else:
            print("Falscher Datentyp!")

    """ BDGraph Funktions-Handler """
    def f_graph_points(self, graph, x_list, y_list):
        if isinstance(graph, dataTypes.BDGraph) and self.is_type_bd_list(x_list, y_list):
            graph.set_points(
                self.get_list_value(x_list),
                self.get_list_value(y_list)
            )
            print(graph.__getstate__())
            return graph
        else:
            print("Falsche Datentypen!")

    # TODO: Was tun mit boolean Argument grid?
    def f_graph_modify(self, graph, x_list, y_list, x_label, y_label, title, grid, label):
        if (isinstance(graph, dataTypes.BDGraph)
                and self.is_type_bd_list(x_list, y_list)
                and self.is_type_string(x_label) and self.is_type_string(y_label)
                and self.is_type_string(title) and self.is_type_string(label)):
            graph.modify_graph(
                self.get_list_value(x_list),
                self.get_list_value(y_list),
                self.get_str_value(x_label),
                self.get_str_value(y_label),
                self.get_str_value(title),
                grid,
                self.get_str_value(label)
            )
            print(graph.__getstate__())
            return graph
        else:
            print("Falsche Datentypen!")

    @staticmethod
    def f_graph_get(graph):
        if isinstance(graph, dataTypes.BDGraph):
            graph.get_graph()
            print(graph.__getstate__())
            return graph
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_graph_set(graph):
        if isinstance(graph, dataTypes.BDGraph):
            graph.set_graph()
            print(graph.__getstate__())
            return graph
        else:
            print("Falscher Datentyp!")

    """ BDImage Funktions-Handler """
    def f_image_resize(self, image, width, height):
        if isinstance(image, dataTypes.BDImage) and self.is_type_int(width) and self.is_type_int(height):
            image.resize(
                self.get_int_value(width),
                self.get_int_value(height)
            )
            print(image.__getstate__())
            return image
        else:
            print("Falsche Datentypen!")

    def f_image_crop(self, image, left, top, right, bottom):
        if ((isinstance(image, dataTypes.BDImage)
             and self.is_type_int(left)
             and self.is_type_int(top))
                and self.is_type_int(right)
                and self.is_type_int(bottom)):
            image.crop(
                self.get_num_value(left),
                self.get_num_value(top),
                self.get_num_value(right),
                self.get_num_value(bottom)
            )
            print(image.__getstate__())
            return image
        else:
            print("Falsche Datentypen!")

    def f_image_filter(self, image, filter_type):
        if isinstance(image, dataTypes.BDImage) and self.is_type_string(filter_type):
            image.apply_filter(self.get_str_value(filter_type))
            print(image.__getstate__())
            return image
        else:
            print("Falsche Datentypen!")

    def f_image_brightness(self, image, factor):
        if isinstance(image, dataTypes.BDImage) and self.is_type_num(factor):
            image.adjust_brightness(self.get_num_value(factor))
            print(image.__getstate__())
            return image
        else:
            print("Falsche Datentypen!")

    @staticmethod
    def f_image_reset(image):
        if isinstance(image, dataTypes.BDImage):
            image.reset()
            print(image.__getstate__())
            return image
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_image_get_size(image):
        if isinstance(image, dataTypes.BDImage):
            image.get_size()
            print(image.__getstate__())
            return image
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_image_show(image):
        if isinstance(image, dataTypes.BDImage):
            image.show()
            print(image.__getstate__())
            return image
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_image_set(image, data):
        if isinstance(image, dataTypes.BDImage) and isinstance(data, dataTypes.BDImage):
            image.set_image(data)
            print(image.__getstate__())
            return image
        else:
            print("Falscher Datentyp!")

    @staticmethod
    def f_image_get(image):
        if isinstance(image, dataTypes.BDImage):
            image.get_image()
            print(image.__getstate__())
            return image
        else:
            print("Falscher Datentyp!")

    """ statische Methoden zur Typ-Überprüfung """
    @staticmethod
    def is_type_bd_int(a, b):
        return isinstance(a, dataTypes.BDInteger) and isinstance(b, dataTypes.BDInteger)

    @staticmethod
    def is_type_bd_float(a, b):
        return isinstance(a, dataTypes.BDFloat) and isinstance(b, dataTypes.BDFloat)

    @staticmethod
    def is_type_bd_string(s1, s2):
        return isinstance(s1, dataTypes.BDString) and isinstance(s2, dataTypes.BDString)

    @staticmethod
    def is_type_string(s):
        return isinstance(s, dataTypes.BDString) or isinstance(s, str)

    @staticmethod
    def is_type_bd_list(l1, l2):
        return isinstance(l1, dataTypes.BDList) and isinstance(l2, dataTypes.BDList)

    @staticmethod
    def is_type_num(x):
        return (isinstance(x, dataTypes.BDInteger)
                or isinstance(x, dataTypes.BDFloat)
                or isinstance(x, int)
                or isinstance(x, float))

    @staticmethod
    def is_type_int(x):
        return isinstance(x, int) or isinstance(x, dataTypes.BDInteger)

    @staticmethod
    def is_type_list(data):
        return isinstance(data, list) or isinstance(data, dataTypes.BDList)

    """ statische Funktionen um den Wert je nach Datentyp zurückzugeben """
    @staticmethod
    def get_int_value(number):
        if isinstance(number, dataTypes.BDInteger):
            return number.__getstate__()
        else:
            return int(number)

    @staticmethod
    def get_num_value(number):
        if isinstance(number, dataTypes.BDInteger) or isinstance(number, dataTypes.BDFloat):
            return number.__getstate__()
        else:
            return float(number)

    @staticmethod
    def get_str_value(s):
        if isinstance(s, dataTypes.BDString):
            return s.__getstate__()
        else:
            return str(s)

    @staticmethod
    def get_list_value(data):
        if isinstance(data, dataTypes.BDList):
            return data.__getstate__()
        else:
            return list(data)



if __name__ == "__main__":
    b_obj = Block()
    print(b_obj.blocks.__len__())
    b_obj.initBlock_Integer_add()