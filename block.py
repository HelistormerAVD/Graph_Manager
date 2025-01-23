import tkinter as tk
from tkinter import filedialog, messagebox
import json

import block_components
import dataTypes
from block_components import TextView, EditText
from dataTypes import BDInteger
from util import h_get_next_empty_dictionary, h_get_vector_between_points


class Block:
    # FIXED VARIABLES

    # Block Höhe = 40 px

    # "B_type" : {"id : 0", "block_id" : 1, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}}
    # "B_components" : {"id" : 0, "component_id" = 1, "c_position" : {}, "data" : dataTypes}
    # "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}


    """Kreiert verschiedene blöcke für den Editor
     (start, end, für flats, für ints, ...)
     """

    def __init__(self):
        self.blockHeight = 40
        self.blocks = {}  # muss in Json gespeichert und geladen werden (in einer Datei)
        self.deletedPos = []  # muss in Json gespeichert und geladen werden (in einer Datei)
        self.editorObjects = {}  # nicht benötigt.
        self.exec_obj = []  # TEMP muss noch auf 0 gesetzt werden beim Laden
        self.funcList = []  # TEMP muss noch auf 0 gesetzt werden beim Laden
        self.loopList = []  # TEMP muss noch auf 0 gesetzt werden beim Laden
        self.tempEntry = None
        # self.blocks[0] = {"B_type" : {"id" : 0, "block_id" : 0, "color": "green2", "connected" : False, "block_inputTypes" : {"input_id" : 0, "input_t" : dataTypes, "inputBlockId" : None}, "block_outputTypes" : {"output_id" : 0, "output_t" : dataTypes, "outputBlockId" : None}, "func" : {"func_name" : "NameOfFunction"}},
        #                  "B_components" : {"id" : 0, "component" : None},
        #                  "B_position" : {"x1": 50, "y1": 50, "x2": 150, "y2": 150}}
        print("done")

    def init_block_start(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text = block_components.TextView()
        b_text.set_data(0, 10, 20, "Start", "black", 10)
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

    def init_block_end(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text = block_components.TextView()
        b_text.set_data(0, 10, 20, "End", "black", 10)
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

    def init_block_set_variable(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view,b_text_view2  = block_components.TextView()
        b_edit_text, b_edit_text2= block_components.EditText()
        b_text_view.set_data(0, 10, 20, "Set Variable", "black", 23)
        b_edit_text.set_data(1, 100, 10, "$VariableName", 10)
        b_text_view2.set_data(0, 175, 20, "to", "black", 10)
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 2,
                "block_tag": "set_variable",
                "color": "dodger blue",
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
                    "func_name": "f_set_variable",
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

    def init_block_integer_add(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view,b_text_view2  = block_components.TextView()
        b_edit_text, b_edit_text2= block_components.EditText()
        b_text_view.set_data(0, 10, 20, "Add Integer", "black", 23)
        b_edit_text.set_data(1, 100, 10, "0", 10)

        b_text_view2.set_data(0, 175, 20, "+", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 3,
                "block_tag": "integer_add",
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
                    "func_name": "f_int_add",
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

    def init_block_integer_sub(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Sub Integer", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "-", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
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

    def init_block_integer_div(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Div Integer", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "/", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 5,
                "block_tag": "integer_div",
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

    def init_block_integer_mult(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Mult Integer", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "+", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 6,
                "block_tag": "integer_mult",
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

    def delete_block(self, block_id):
        self.blocks[block_id] = {}
        self.deletedPos[block_id].append(block_id)

    def find_block_id_from_canvas(self, canvas_id):
        stop_alg = 0
        for i in range(self.blocks.__len__()):
            if self.deletedPos:
                for j in self.deletedPos:
                    if j == i:
                        print("was Deletes")
                        stop_alg = 1
                    else:
                        print(f"J = {j}, canvasId = {canvas_id}")
                        print(f"block: {self.blocks[i]} Deleted Pos: {self.deletedPos}")
                        stop_alg = 0
                        if self.blocks[i]["B_type"]["id"] == canvas_id:
                            return i
                    if stop_alg == 1:
                        print("skipped")
            else:
                if self.blocks[i]["B_type"]["id"] == canvas_id:
                    return i
        return None

    def set_block_position(self, block_id, x1, y1, x2, y2):
        self.blocks[block_id]["B_position"] = {"x1": x1, "y1": y1, "x2": x2, "y2": y2}

    def get_block_position(self, block_id):
        return self.blocks[block_id]["B_position"]

    def get_block_type(self, block_id):
        return self.blocks[block_id]["B_type"]

    def set_block_components(self, block_id, comp_id, comp):
        count = len(self.blocks[block_id]["B_components"])
        if comp_id < count:
            self.blocks[block_id]["B_components"][comp_id] = comp
            return 1
        else:
            return 0

    def move_block(self, block_id, x1, y1):
        old_pos = self.get_block_position(block_id)
        self.blocks[block_id]["B_position"] = {"x1": x1, "y1": y1, "x2": x1 + (old_pos["x2"] - old_pos["x1"]),
                                               "y2": y1 + (old_pos["y2"] - old_pos["y1"])}

    def move_block_relativ(self, block_id, x1, y1):
        old_pos = self.get_block_position(block_id)
        dx, dy = h_get_vector_between_points(x1, y1, old_pos["x1"], old_pos["y1"])
        self.blocks[block_id]["B_position"] = {"x1": (old_pos["x1"] + dx), "y1": (old_pos["y1"] + dy),
                                               "x2": (old_pos["x2"] + dx), "y2": (old_pos["y2"] + dy)}

    def set_all_block_components(self, block_id, comp):
        self.blocks[block_id]["B_components"] = comp

    # --------------------------------------------------------------------------------------------------------------------------------
    #
    #                       Funktionen für Blöcke

    # float / double
    def init_block_float_add(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Add Float", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "+", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = []
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 7,
                "block_tag": "float_add",
                "color": "royal blue",
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
                    "func_name": "f_float_add",
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

    def init_block_float_sub(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Sub Float", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "-", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
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
                    "input_t": dataTypes.BDFloat,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat,
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

    def init_block_float_div(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Div Float", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "/", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
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
                    "input_t": dataTypes.BDFloat,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat,
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

    def init_block_float_mult(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Mult Float", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "*", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
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
                    "input_t": dataTypes.BDFloat,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 1,
                    "output_t": dataTypes.BDFloat,
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
    def init_block_str_concat(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Str_Concat", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "first", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "with", "black", 23)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 225, 10, "secund", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
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
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
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
    def init_block_str_sub_div(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "String subDiv", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, " ", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1,3]
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
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
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

    def init_block_str_trim(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Str_trim", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "text", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(1, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})

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
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
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

    def init_block_str_split(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Str_split", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "zeichen", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "in", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "text", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
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
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
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

    def init_block_str_find(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "find Str", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "String", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "in", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "text", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
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
                    "input_t": dataTypes.BDString,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 2,
                    "output_t": dataTypes.BDString,
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

    def init_block_function(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Function", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "f_nameOfFunction", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        args = [1]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 16,
                "block_tag": "funcBlock",
                "color": "teal",
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
                "x2": 350,
                "y2": 90}
        }
        return index

    def init_block_goto(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Goto", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "f_nameOfFunction", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 17,
                "block_tag": "goto",
                "color": "teal",
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
                "x2": 350,
                "y2": 90}
        }
        return index

    def init_block_function_return(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "return to", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "f_nameOfFunction", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 18,
                "block_tag": "funcReturn",
                "color": "teal",
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
                "x2": 350,
                "y2": 90}
        }
        return index

    def init_block_if(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "if", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        args = [1]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 19,
                "block_tag": "if",
                "color": "aqua",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDInteger(0),  # 01 true false
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDInteger(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_nop",
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

    def init_block_while_loop_end(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Loop End", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "l_test", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        args = [1]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 20,
                "block_tag": "whileLoopEnd",
                "color": "dark cyan",
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

    def init_block_while_loop(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "While-Loop", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "l_test", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "1 ==", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "0", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 21,
                "block_tag": "whileLoop",
                "color": "aquamarine",
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


    def init_block_list_insert(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Insert in list", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "Wert", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "in", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "Liste", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 22,
                "block_tag": "list_insert",
                "color": "mediumpurple",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDList(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDList(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_list_insert",
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

    def init_block_list_get(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "get List", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "liste", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(1, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})

        args = [0]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 23,
                "block_tag": "list_get",
                "color": "mediumpurple",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDList(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDList(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_list_get",
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

    def init_block_list_delete(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "delete List", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "liste", 10)

        components = []

        components.insert(0, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(1, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})

        args = [0]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 24,
                "block_tag": "list_delete",
                "color": "mediumpurple",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDList(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDList(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_list_delete",
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

    def init_block_list_sort(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "sort List", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "Liste", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "mit", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "sort_art", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 25,
                "block_tag": "list_sort",
                "color": "mediumpurple",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDList(0),
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 0,
                    "output_t": dataTypes.BDList(0),
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_list_sort",
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

    def init_block_set_graph(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Set Graph  x:", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "x-werte", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "y:", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "y-werte", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 26,
                "block_tag": "set_graph",
                "color": "gold",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 0,
                    "input_t": dataTypes.BDInteger,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 4,
                    "output_t": dataTypes.BDGraph,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_set_graph",
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

    # def modify_graph(self, x, y, x_label, y_label, title, grid, label):

    def init_block_modify_graph(self):

        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "modify Graph", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 120, 10, "graph", 10)

        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 200, 20, "x:", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 225, 10, "wert", 10)

        b_text_view3 = block_components.TextView()
        b_text_view3.set_data(0, 300, 20, "y:", "black", 10)
        b_edit_text3 = block_components.EditText()
        b_edit_text3.set_data(1, 325, 10, "wert", 10)

        b_text_view4 = block_components.TextView()
        b_text_view4.set_data(0, 400, 20, "x-label", "black", 10)
        b_edit_text4 = block_components.EditText()
        b_edit_text4.set_data(1, 450, 10, "label", 10)

        b_text_view5 = block_components.TextView()
        b_text_view5.set_data(0, 530, 20, "y-label", "black", 10)
        b_edit_text5 = block_components.EditText()
        b_edit_text5.set_data(1, 580, 10, "label", 10)

        b_text_view6 = block_components.TextView()
        b_text_view6.set_data(0, 680, 20, "title", "black", 10)
        b_edit_text6 = block_components.EditText()
        b_edit_text6.set_data(1, 730, 10, "titel", 10)

        b_text_view7 = block_components.TextView()
        b_text_view7.set_data(0, 810, 20, "grid", "black", 10)
        b_edit_text7 = block_components.EditText()
        b_edit_text7.set_data(1, 860, 10, "grid", 10)

        b_text_view8 = block_components.TextView()
        b_text_view8.set_data(0, 940, 20, "label", "black", 10)
        b_edit_text8 = block_components.EditText()
        b_edit_text8.set_data(1, 990, 10, "label", 10)

        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})
        components.insert(4, {"id": None, "component_id": 0, "entry": None, "component": b_text_view3})
        components.insert(5, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text3})
        components.insert(6, {"id": None, "component_id": 0, "entry": None, "component": b_text_view4})
        components.insert(7, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text4})
        components.insert(8, {"id": None, "component_id": 0, "entry": None, "component": b_text_view5})
        components.insert(9, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text5})
        components.insert(10, {"id": None, "component_id": 0, "entry": None, "component": b_text_view6})
        components.insert(11, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text6})
        components.insert(12, {"id": None, "component_id": 0, "entry": None, "component": b_text_view7})
        components.insert(13, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text7})
        components.insert(14, {"id": None, "component_id": 0, "entry": None, "component": b_text_view8})
        components.insert(15, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text8})

        args = [1, 3, 5, 7, 9, 11, 13, 15]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 27,
                "block_tag": " modi_graph",
                "color": "goldenrod",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 4,  # ????
                    "input_t": dataTypes.BDGraph,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 4,
                    "output_t": dataTypes.BDGraph,
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
                "x2": 1100,
                "y2": 90}
        }
        return index

    def init_block_get_graph(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Get Graph", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "graph", 10)

        components = []
        components.insert(0, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(1, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        args = [0]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 28,
                "block_tag": "get_graph",
                "color": "gold",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 4,
                    "input_t": dataTypes.BDGraph,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 4,
                    "output_t": dataTypes.BDGraph,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_get_graph",
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

    def init_block_load_file_in_list(self):
        index = h_get_next_empty_dictionary(self.blocks)
        for i in range(len(self.deletedPos)):
            if index == self.deletedPos[i]:
                self.deletedPos.pop(i)
        b_text_view = block_components.TextView()
        b_text_view.set_data(0, 10, 20, "Load File", "black", 23)
        b_edit_text = block_components.EditText()
        b_edit_text.set_data(1, 100, 10, "<path>", 10)
        b_text_view2 = block_components.TextView()
        b_text_view2.set_data(0, 175, 20, "in List", "black", 10)
        b_edit_text2 = block_components.EditText()
        b_edit_text2.set_data(1, 200, 10, "<ListVar>", 10)
        components = []
        components.insert(0, {"id": None, "component_id": 0, "entry": None, "component": b_text_view2})
        components.insert(1, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text})
        components.insert(2, {"id": None, "component_id": 0, "entry": None, "component": b_text_view})
        components.insert(3, {"id": None, "component_id": 1, "entry": None, "component": b_edit_text2})

        args = [1, 3]
        self.blocks[index] = {
            "B_type": {
                "id": None,
                "block_id": 27,
                "block_tag": " modi_graph",
                "color": "goldenrod",
                "connected": False,
                "inLoop": False,
                "block_inputTypes": {
                    "input_id": 4,
                    "input_t": dataTypes.BDGraph,
                    "inputBlockId": None},
                "block_outputTypes": {
                    "output_id": 4,  # ???
                    "output_t": dataTypes.BDGraph,
                    "outputBlockId": None},
                "func": {
                    "func_name": "f_modi_graph",
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
    # --------------------------------------------------------------------------------------------------------------------------------

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
            a.BDInteger.subtract(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    def f_int_mul(self, a, b):
        if self.is_type_bd_int(a, b):
            a.BDInteger.multiply(b.__getstate__())
            print(a.__getstate__())
            return a
        else:
            print("Falscher Datentyp!")

    # BDFloat divide Funktion???
    def f_int_div(self, a, b):
        if self.is_type_bd_int(a, b):
            a.BDFloat.divide(b.__getstate__())
            print(a.__getstate__())
            return a
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
            a.BDInteger.divide(b.__getstate__())
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
    b_obj.init_block_integer_add()
