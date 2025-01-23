import tkinter as tk
from tkinter import *
import json

import block
from tkinter import filedialog, messagebox

import block_components
import dataTypes
from script_variables import Var
from util import h_get_next_empty_dictionary, h_get_vector_between_points, h_convert_to_data_types_from_string
from functools import partial


class BlockEditorView:

    def __init__(self, root):
        self.root = root
        self.root.title("Block-Based Graphical Editor")

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Sidebar (left side)
        self.sidebarRight = tk.Frame(self.main_frame, bg="lightgray", width=200)
        self.sidebarRight.pack(side=tk.RIGHT, fill=tk.Y)

        self.sidebarLeft = tk.Frame(self.main_frame, bg="lightgray", width=200)
        self.sidebarLeft.pack(side=tk.LEFT, fill=tk.Y)

        # Canvas (right side)
        self.canvas = tk.Canvas(self.main_frame, bg="white", width=1080, height=720)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Toolbar (top)
        self.toolbar = tk.Frame(root, bg="lightgray")
        self.toolbar.pack(fill=tk.X)

        self.add_block_button = tk.Button(self.toolbar, text="Select", command=lambda: self.switch_editor_tool(0))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Add Block",
                                          command=lambda: self.add_block("initBlock_modify_Graph"))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Move", command=lambda: self.switch_editor_tool(1))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Link", command=lambda: self.switch_editor_tool(2))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Delete", command=self.on_delete_block)
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.execute_button = tk.Button(self.toolbar, text="Execute", command=self.on_execute_script)
        self.execute_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.Save_button = tk.Button(self.sidebarRight, text="Save", command=self.on_save_editor)
        self.Save_button.pack(side=tk.TOP, padx=5, pady=5)

        self.Load_button = tk.Button(self.sidebarRight, text="Load", command=self.on_load_editor)
        self.Load_button.pack(side=tk.TOP, padx=5, pady=5)

        self.Load_button = tk.Button(self.sidebarLeft, text="Toggle Fold", command=self.on_load_editor)
        self.Load_button.pack(side=tk.TOP, padx=5, pady=5)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu, background="#729ecf")

        self.blockMenuInteger = Menu(self.menu)
        self.blockMenuInteger.configure(background="#6164e0")
        self.blockMenuInteger.add_command(label="Integer Addition",
                                          command=lambda: self.add_block("initBlock_Integer_add"))
        self.blockMenuInteger.add_command(label="Integer Subtraction",
                                          command=lambda: self.add_block("initBlock_Integer_sub"))
        self.blockMenuInteger.add_command(label="Integer Multiplication",
                                          command=lambda: self.add_block("initBlock_Integer_mult"))
        self.blockMenuInteger.add_command(label="Integer Division",
                                          command=lambda: self.add_block("initBlock_Integer_div"))
        self.menu.add_cascade(label="Integer", menu=self.blockMenuInteger)
        self.blockMenuFloat = Menu(self.menu)
        self.blockMenuFloat.configure(background="#6164e0")
        self.blockMenuFloat.add_command(label="Float Addition", command=lambda: self.add_block("initBlock_Float_add"))
        self.blockMenuFloat.add_command(label="Float Subtraction",
                                        command=lambda: self.add_block("initBlock_Float_sub"))
        self.blockMenuFloat.add_command(label="Float Multiplication",
                                        command=lambda: self.add_block("initBlock_Float_mult"))
        self.blockMenuFloat.add_command(label="Float Division", command=lambda: self.add_block("initBlock_Float_div"))
        self.menu.add_cascade(label="Float", menu=self.blockMenuFloat)
        self.blockMenuString = Menu(self.menu)
        self.blockMenuString.configure(background="#6164e0")
        self.blockMenuString.add_command(label="String Concat", command=lambda: self.add_block("initBlock_Str_concat"))
        self.blockMenuString.add_command(label="String Subdivide",
                                         command=lambda: self.add_block("initBlock_Str_subDiv"))
        self.blockMenuString.add_command(label="String Trim", command=lambda: self.add_block("initBlock_Str_trim"))
        self.blockMenuString.add_command(label="String Split", command=lambda: self.add_block("initBlock_Str_split"))
        self.blockMenuString.add_command(label="String Find", command=lambda: self.add_block("initBlock_Str_find"))
        self.menu.add_cascade(label="String", menu=self.blockMenuString)
        self.blockMenuList = Menu(self.menu)
        self.blockMenuList.configure(background="#6164e0")
        self.menu.add_cascade(label="List", menu=self.blockMenuList)
        self.blockMenuGraph = Menu(self.menu)
        self.blockMenuGraph.configure(background="#6164e0")

        self.blockMenuGraph.configure(background="#6164e0")
        self.blockMenuGraph.add_command(label="Set Graph", command=lambda: self.add_block("initBlock_set_Graph"))
        self.blockMenuGraph.add_command(label="modify Graph", command=lambda: self.add_block("initBlock_modify_Graph"))
        self.blockMenuGraph.add_command(label="Get Graph", command=lambda: self.add_block("initBlock_get_Graph"))

        self.menu.add_cascade(label="Graph", menu=self.blockMenuGraph)
        self.blockMenuControl = Menu(self.menu)
        self.blockMenuControl.configure(background="#6164e0")
        self.blockMenuControl.add_command(label="Function", command=lambda: self.add_block("initBlock_Function"))
        self.blockMenuControl.add_command(label="Goto Function", command=lambda: self.add_block("initBlock_Goto"))
        self.blockMenuControl.add_command(label="return to Goto call",
                                          command=lambda: self.add_block("initBlock_FunctionReturn"))
        self.menu.add_cascade(label="Flow Control", menu=self.blockMenuControl)
        self.blockMenuMisc = Menu(self.menu)
        self.blockMenuMisc.configure(background="#6164e0")
        self.blockMenuMisc.add_command(label="Function", command=lambda: self.add_block("initBlock_setVariable"))
        self.menu.add_cascade(label="Misc", menu=self.blockMenuMisc)

        self.b_obj = block.Block()
        self.g_var = Var()

        self.selectedTool = 1
        self.END_OF_SCRIPT = 0

        self.selectedBlockItem = None
        self.selectedBlockId = None
        self.selectedBlockCanvasId = None

        self.lastSelectedBlockItem = None
        self.lastSelectedBlockId = None
        self.lastSelectedBlockCanvasId = None

        self.on_start_up()

        # self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Button-2>", self.on_canvas_click)
        self.canvas.focus_set()  # Set focus to the canvas
        self.canvas.bind("<Button-3>", self.debug_click)
        self.canvas.focus_set()  # Set focus to the canvas
        self.canvas.bind("<Key-q>", self.debug_hotkey1)
        self.canvas.bind("<Key-w>", self.debug_hotkey2)
        self.canvas.bind("<Key-e>", self.debug_hotkey3)
        # self.canvas.bind("<B1-Motion>", self.on_canvas_drag)

    def debug_hotkey1(self, event):
        self.switch_editor_tool(0)

    def debug_hotkey2(self, event):
        self.switch_editor_tool(1)

    def debug_hotkey3(self, event):
        self.switch_editor_tool(2)

    def on_start_up(self):
        start_block = self.add_block("initBlock_start")
        self.b_obj.move_block(start_block, 400, 100)
        end_block = self.add_block("initBlock_end")
        self.b_obj.move_block(end_block, 400, 600)
        self.update_block_position(start_block)
        self.update_block_position(end_block)

    def add_block(self, func_name: str):
        index = eval("self.b_obj." + func_name + "()")
        # index = self.b_obj.initBlock_Integer_add()
        new_block = self.b_obj.blocks[index]
        b_comp_length = new_block["B_components"].__len__()
        # print(new_block["B_components"])
        new_block["B_type"]["id"] = self.canvas.create_rectangle(new_block["B_position"]["x1"],
                                                                new_block["B_position"]["y1"],
                                                                new_block["B_position"]["x2"],
                                                                new_block["B_position"]["y2"],
                                                                fill=new_block["B_type"]["color"],
                                                                tags=["Block", new_block["B_type"]["block_tag"]])
        for i in range(b_comp_length):
            component_type = None
            component_id = new_block["B_components"].__getitem__(i)["component_id"]
            match component_id:
                case 0:
                    text_view_settings = new_block["B_components"].__getitem__(i)["component"].get_data()
                    text_view_comp = self.canvas.create_text(text_view_settings["x1"] + new_block["B_position"]["x1"],
                                                           text_view_settings["y1"] + new_block["B_position"]["y1"],
                                                           text=text_view_settings["text"],
                                                           fill=text_view_settings["fontColor"], tags="TextView",
                                                           font=('Helvetica', '12'), anchor="w")
                    new_block["B_components"].__getitem__(i)["id"] = text_view_comp
                    # self.b_obj.editorObjects[indexOfCanvasObject]["components"].append({"Id" : text_view_comp, "type" : "TextView"})
                case 1:
                    edit_text_settings = new_block["B_components"].__getitem__(i)["component"].get_data()
                    component_type = tk.Entry(self.root, width=edit_text_settings["width"])
                    component_type.insert(0, edit_text_settings["text"])
                    edit_text_comp = self.canvas.create_window(edit_text_settings["x1"] + new_block["B_position"]["x1"],
                                                             edit_text_settings["y1"] + new_block["B_position"]["y1"],
                                                             window=component_type,
                                                             anchor="nw",
                                                             tags="EditText")
                    # self.b_obj.editorObjects[indexOfCanvasObject]["components"].append({"Id" : edit_text_comp, "type" : "EditText"})
                    new_block["B_components"].__getitem__(i)["id"] = edit_text_comp
                    new_block["B_components"].__getitem__(i)["entry"] = component_type

                    # new_block["B_components"][component_id]["id"] = edit_text_comp
                    print(new_block)
        return index

    def switch_editor_tool(self, tool_number):
        if tool_number < 0 or tool_number > 3:
            print("wrong tool to be selected")
        else:
            self.selectedTool = tool_number

    def set_selected_block(self, *args):
        x = 0
        y = 0
        if args:
            print(args)
            if args.__len__() > 1:
                x = args[0]
                y = args[1]
            else:
                print("Cant find position to select from!")
        item = self.canvas.find_closest(x, y, start="Block")
        if item:
            if self.selectedBlockItem:
                self.lastSelectedBlockItem = self.selectedBlockItem
                self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                self.lastSelectedBlockId = self.selectedBlockId
                self.selectedBlockItem = item
                self.selectedBlockCanvasId = item[0]
                self.selectedBlockId = self.b_obj.find_block_id_from_canvas(item[0])
                return 1
            else:
                if self.selectedBlockItem != self.lastSelectedBlockItem:
                    self.lastSelectedBlockItem = self.selectedBlockItem
                    self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                    self.lastSelectedBlockId = self.selectedBlockId
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.find_block_id_from_canvas(item[0])
                    return 1
                else:
                    self.lastSelectedBlockItem = self.selectedBlockItem
                    self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                    self.lastSelectedBlockId = self.selectedBlockId
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.find_block_id_from_canvas(item[0])
                    return 1
        else:
            print("err")
            return 0

    #    def set_selected_block(self, event):
    #        """ Setzt den ausgewählten Block und aktualisiert letzten ausgewählten Block """
    #        item = self.canvas.find_closest(event.x, event.y, start="Block")
    #        if not item:    # kein nächster Block
    #            if self.selectedBlockItem:  # es gibt ausgewählten Block
    #                # last -> current, current -> None
    #                self.lastSelectedBlockItem = self.selectedBlockItem
    #                self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
    #                self.lastSelectedBlockId = self.selectedBlockId
    #                self.selectedBlockItem = None
    #                self.selectedBlockCanvasId = None
    #                self.selectedBlockId = None
    #            return 1
    #
    #        # nächster Block gefunden
    #        if not self.selectedBlockItem:    # wenn kein ausgewählter Block
    #            # current -> item, last nicht verändern
    #            self.selectedBlockItem = item
    #            self.selectedBlockCanvasId = item[0]
    #            self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
    #            return 1
    #
    #        # neuer ausgewählter Block + Block war ausgewählt
    #        if self.selectedBlockId != self.b_obj.findBlockIdFromCanvas(item[0]):
    #            # last -> current, current -> item
    #            self.lastSelectedBlockItem = self.selectedBlockItem
    #            self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
    #            self.lastSelectedBlockId = self.selectedBlockId
    #            self.selectedBlockItem = item
    #            self.selectedBlockCanvasId = item[0]
    #            self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
    #        else:
    #            pass    # derselbe Block wurde erneut ausgewählt: Nichts tun
    #        return 1

    def check_dual_selection(self):
        if self.selectedBlockItem and self.lastSelectedBlockItem:
            return 1
        else:
            return 0

    def check_dual_selection_is_same(self):
        if self.selectedBlockId == self.lastSelectedBlockId:
            return 1
        else:
            return 0

    """
        if self.selectedBlockItem:
            if self.lastSelectedBlockItem:
                if item:
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.selectedBlockItem = None
                    self.selectedBlockCanvasId = None
                    self.selectedBlockId = None
                    return 0
            else:
                if item:
                    self.lastSelectedBlockItem = self.selectedBlockItem
                    self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                    self.lastSelectedBlockId = self.selectedBlockId
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.selectedBlockItem = None
                    self.selectedBlockCanvasId = None
                    self.selectedBlockId = None
                    return 0
        else:
            if self.lastSelectedBlockItem:
                if item:
                    self.selectedBlockItem = self.lastSelectedBlockItem
                    self.selectedBlockCanvasId = self.lastSelectedBlockCanvasId
                    self.selectedBlockId = self.lastSelectedBlockId
                    self.lastSelectedBlockItem = None
                    self.lastSelectedBlockId = None
                    self.lastSelectedBlockCanvasId = None
                    return 1
                else:
                    self.selectedBlockItem = self.lastSelectedBlockItem
                    self.selectedBlockCanvasId = self.lastSelectedBlockCanvasId
                    self.selectedBlockId = self.lastSelectedBlockId
                    self.lastSelectedBlockItem = None
                    self.lastSelectedBlockId = None
                    self.lastSelectedBlockCanvasId = None
                    return 0
            else:
                if item:
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.selectedBlockItem = None
                    self.selectedBlockCanvasId = None
                    self.selectedBlockId = None
                    return 0
    """

    # cur last item : Block Ausgewählt | Letzter Ausgewählter Block | nächster Ausgewählter Block
    #   0   0   0   : nein, nein, nein -> alles auf None setzen.
    #   0   0   1   : es gibt einen Block aber es wurde noch nichts ausgewählt -> nur current = item
    #   0   1   0   : keinen aktuellen Block, es gab einen Block, aber keinen neuer -> alles auf None (da wir nicht wissen, ob der Block noch existiert)
    #   0   1   1   : keinen selected Block, es gab einen Block, und es gibt einen neuen -> current = item, last = None (da wir nicht wissen, ob der Block noch existiert)
    #   1   0   0   : ausgewählter block, kein letzten, kein neuer -> last = current, current = None
    #   1   0   1   : ausgewählter block, kein letzten, aber neuer -> last = current, current = item
    #   1   1   0   : ausgewählter block, es gibt einen letzten, kein neuer -> nichts
    #   1   1   1   : ausgewählter block, es gibt einen letzten, und einen neuen -> last = current, current = item

    def on_canvas_click(self, event):
        match self.check_selected_tool():
            case 1:
                block_id = self.selectedBlockId
                self.set_selected_block(event.x, event.y)
                self.update_all_blocks_appearance()
            case 2:
                if self.selectedBlockItem:
                    block_id = self.selectedBlockId
                    if not self.b_obj.blocks[block_id]["B_type"]["connected"]:
                        self.b_obj.move_block(block_id, event.x, event.y)
                        self.update_block_position(block_id)
                        # self.updateBlockAppearance(block_id)
                    self.update_all_blocks_appearance()
                else:
                    print("no Block Selected")
            case 3:
                if self.selectedBlockItem:
                    self.on_create_link(self.selectedBlockId, self.lastSelectedBlockId)
                else:
                    print("no Block Selected")
            case 4:
                if self.selectedBlockItem:
                    block_id = self.selectedBlockId
                    self.on_delete_block(block_id, self.selectedBlockItem)
                else:
                    print("no Block Selected")

    def on_create_link(self, block_id, selected_block_id):
        """ erstellt einen Link zwischen den beiden Blöcken mit den block_ids block_id und selected_block_id """
        print("create a link between two blocks")
        if not self.check_dual_selection_is_same():
            if block_id != None and selected_block_id != None:
                block_dict = self.b_obj.blocks[block_id]["B_type"]
                selected_block_dict = self.b_obj.blocks[selected_block_id]["B_type"]

                # selected_block_dict["block_inputTypes"]["input_t"] = block_dict["block_outputTypes"]["output_t"]
                selected_block_dict["block_inputTypes"]["inputBlockId"] = block_id
                selected_block_dict["connected"] = True

                block_dict["block_outputTypes"]["outputBlockId"] = selected_block_id
                block_dict["connected"] = True

                block_height = self.b_obj.blockHeight
                pos = self.b_obj.get_block_position(block_id)

                x1 = pos["x1"]  # 10 da jede umrandung die hälfte nach innen und außen ist
                y1 = pos["y1"] + block_height

                self.b_obj.move_block(selected_block_id, x1, y1)
                self.update_block_position(selected_block_id)
                self.update_all_blocks_appearance()
                print("link created")
        else:
            print(f"block_id {block_id} and selected_block_id {selected_block_id} must not be equal")
        # überprüfe, ob block_id == selected_block_id (darf nicht die selbe sein)
        #   in block-dict vom selected_block_id füge "inputBlockId" = block_id
        #   in block-dict vom selected_block_id füge "input_t" = dataTypes vom block_id "output_t"
        #   in block-dict vom block_id füge "outputBlockId" = selected_block_id
        #   in block-dict vom block_id setze "connected" = True
        #   in block-dict vom selected_block_id setze "connected" = True
        #   funktion moveBlock(aus b_obj) mit selected_block_id an x1 von block_id und (y2 von block_id) + Blockhöhe (40)

    def on_delete_block(self):
        block_id = self.selectedBlockId
        print("deletes a block from the Canvas and from block-dict. (self.b_obj.blocks[index])")
        canvas_id = self.b_obj.blocks[block_id]["B_type"]["id"]
        last_block_pos_x = self.b_obj.blocks[block_id]["B_position"]["x1"]
        last_block_pos_y = self.b_obj.blocks[block_id]["B_position"]["y1"]
        block = self.b_obj.blocks[block_id]["B_type"]
        if block["block_id"] == 0 or block["block_id"] == 1:
            print("cannot delete Start-Block or End-Block!")
            return 0
        if block["connected"]:
            if block["block_inputTypes"]["inputBlockId"]:
                self.b_obj.blocks[block["block_inputTypes"]["inputBlockId"]]["block_outputTypes"][
                    "outputBlockId"] = None
            if block["block_outputTypes"]["outputBlockId"]:
                self.b_obj.blocks[block["block_outputTypes"]["outputBlockId"]]["block_inputTypes"][
                    "inputBlockId"] = None
        self.b_obj.deletedPos.append(block_id)
        for comp in self.b_obj.blocks[block_id]["B_components"]:
            self.canvas.delete(comp["id"])
        self.canvas.delete(canvas_id)
        self.b_obj.blocks[block_id] = {}
        self.set_selected_block(last_block_pos_x, last_block_pos_y)
        self.update_all_blocks_appearance()
        # überprüfe, od es der Startblock ist (der darf nicht gelöscht werden)
        # überprüfe, ob block_id == selected_block_id
        #   lösche block_id vom Canvas
        #   lösche block_id vom block-dict.
        #   setze self.selectedBlock auf None
        # ansonsten print("fehler")
        print("deleted")
        return 1

    def on_disconnect_link(self):
        print("diconnected Block")

    def exec_compile_execution(self):
        self.b_obj.funcList = []
        print("####EMPTY!!!!")
        func_blocks = self.canvas.find_withtag("funcBlock")
        print(func_blocks)
        for i in func_blocks:
            block = self.b_obj.blocks[self.b_obj.find_block_id_from_canvas(i)]
            print("Block: " + block.__str__())
            block_component_list = block["B_components"]
            print("i = " + i.__str__())
            print(block_component_list.__len__())
            for j in range(block_component_list.__len__()):
                comp = block_component_list[j]
                if comp["entry"]:
                    comp_input_text = comp["entry"].get()
                    self.b_obj.funcList.append({"funcName": comp_input_text, "block_canvas_id": i,
                                                "block_id": self.b_obj.find_block_id_from_canvas(i),
                                                "return_block_id": None})
        print("####FULL!!!!")
        print(self.b_obj.funcList)

    def on_execute_script(self):
        self.exec_compile_execution()
        start_block_canvas_id = self.canvas.find_withtag("start")[0]
        current_block = self.b_obj.blocks[self.b_obj.find_block_id_from_canvas(start_block_canvas_id)]
        block_id = self.b_obj.find_block_id_from_canvas(start_block_canvas_id)
        not_executed = False
        if not current_block["B_type"]["block_outputTypes"]["outputBlockId"]:
            print("[Compiler]: nothing connected to Start block!")
            return 0
        self.exec_evaluate_function(block_id)

        while self.END_OF_SCRIPT == 0:
            if self.exec_has_reached_end_of_script(block_id):
                print("[Execute]: end of Script reached!")
                break
            else:
                if not_executed:
                    data_type_obj = self.exec_evaluate_function(block_id)
                    block_id, current_block, not_executed = self.exec_check_structure_blocks(block_id, current_block,
                                                                                           not_executed)
                    if type(self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["output_t"]) == type(
                            data_type_obj):
                        self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["output_t"] = data_type_obj
                    not_executed = False
                else:
                    if current_block["B_type"]["block_outputTypes"]["outputBlockId"]:
                        block_id = current_block["B_type"]["block_outputTypes"]["outputBlockId"]
                        current_block = self.b_obj.blocks[current_block["B_type"]["block_outputTypes"]["outputBlockId"]]
                        data_type_obj = self.exec_evaluate_function(block_id)
                        block_id, current_block, not_executed = self.exec_check_structure_blocks(block_id, current_block,
                                                                                               not_executed)
                        # data_type_obj = self.exec_evaluateFunction(block_id)
                        if type(self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["output_t"]) == type(
                                data_type_obj):
                            self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["output_t"] = data_type_obj
                    else:
                        print("[Compiler]: nothing connected to next block!")
                        return 1

    """ def onExecuteScript(self):
        self.exec_compileExecution()
        startBlockCanvasId = self.canvas.find_withtag("start")[0]
        currentBlock = self.b_obj.blocks[self.b_obj.findBlockIdFromCanvas(startBlockCanvasId)]
        block_id = self.b_obj.findBlockIdFromCanvas(startBlockCanvasId)
        if not currentBlock["B_type"]["block_outputTypes"]["outputBlockId"]:
            print("[Compiler]: nothing connected to Start block!")
            return 0
        self.exec_evaluateFunction(block_id)

        while self.END_OF_SCRIPT == 0:
            if self.exec_hasReachedEndOfScript(block_id):
                print("[Execute]: end of Script reached!")
                break
            else:
                if currentBlock["B_type"]["block_outputTypes"]["outputBlockId"]:
                    block_id = currentBlock["B_type"]["block_outputTypes"]["outputBlockId"]
                    currentBlock = self.b_obj.blocks[currentBlock["B_type"]["block_outputTypes"]["outputBlockId"]]
                    block_id, currentBlock = self.exec_checkStructureBlocks(block_id, currentBlock)
                    dataTypeObj = self.exec_evaluateFunction(block_id)
                    if type(self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["output_t"]) == type(dataTypeObj):
                        self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["output_t"] = dataTypeObj
                else:
                    print("[Compiler]: nothing connected to next block!")
                    return 1"""

    """ Variablen für die Funktion: """
    # startBlock_id: finde die ID des Startblocks in b_obj.blocks
    # nextBlock_id: finde die nächste block_id vom Block, welcher als "outputBlockId" im StartBlock-dict. gespeichert ist.
    # functionName: <speichert die Funktion als name, die von einem Block ausgeführt werden soll.> Anfangs str
    # functionArgs: <speichert die Args für die function, welche von einem Block ausgeführt werden soll. Wird als dataTypes gespeichert.> Anfangs None
    # f_executeEnd: Flag, wenn das ende der verlinkten Blöcke erreicht wurde.
    # f_executeBreak: Flag, wenn die exeution abgebrochen werden muss, falls es z.B. einen Fehler gibt.
    # f_executesuccess: Flag, wenn execution geklappt hat.
    """-----------------------------"""

    # testet, ob der aktuelle Block ein Struktur Block ist.
    def exec_check_structure_blocks(self, block_id, current_block, dont_skip):
        print("------START-------")
        block = self.b_obj.blocks[block_id]["B_type"]
        print("Block: " + block.__str__())
        block_component_list = self.b_obj.blocks[block_id]["B_components"]
        print("CompList: " + block_component_list.__str__())
        for i in range(block_component_list.__len__()):
            comp = block_component_list[i]
            if comp["entry"]:
                comp_input_text = comp["entry"].get()
                print("Hat Entry gefunden: " + comp_input_text)
                if block["block_id"] == 17:  # wenn goto block, dann finde den passenden Funktionsblock
                    print("ist Block_id 17? : " + block["block_id"].__str__())
                    if comp_input_text.startswith("f_", 0, 2):
                        print("startet Mit f_ !")
                        print("funcList länge: " + self.b_obj.funcList.__len__().__str__())
                        for j in range(self.b_obj.funcList.__len__()):
                            print(
                                "funcName: " + self.b_obj.funcList.__getitem__(j)["funcName"] + " == " + comp_input_text)
                            if self.b_obj.funcList.__getitem__(j)["funcName"] == comp_input_text:
                                self.b_obj.funcList.__getitem__(j)["return_block_id"] = block_id
                                block_id = self.b_obj.funcList.__getitem__(j)["block_id"]
                                current_block = self.b_obj.blocks[
                                    block_id]  # self.b_obj.blocks[self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["outputBlockId"]]
                                dont_skip = True
                                print("DOCH!!!")
                                print(current_block)
                                return block_id, current_block, dont_skip
                elif block["block_id"] == 18:  # wenn goto block, dann finde den passenden Block unter dem Goto Block
                    if comp_input_text.startswith("f_", 0, 2):
                        print("startet Mit f_ !")
                        print("funcList länge: " + self.b_obj.funcList.__len__().__str__())
                        for j in range(self.b_obj.funcList.__len__()):
                            print(
                                "funcName: " + self.b_obj.funcList.__getitem__(j)["funcName"] + " == " + comp_input_text)
                            if self.b_obj.funcList.__getitem__(j)["funcName"] == comp_input_text:
                                return_block_id = self.b_obj.funcList.__getitem__(j)["return_block_id"]
                                print("Blocks: " + return_block_id.__str__())
                                all_blocks = self.canvas.find_withtag("Block")
                                print("Blocks: " + all_blocks.__str__())
                                for k in all_blocks:
                                    iterated_block = self.b_obj.blocks[self.b_obj.find_block_id_from_canvas(k)]
                                    print("iterated_block: " + iterated_block.__str__())
                                    if iterated_block["B_type"]["connected"]:
                                        print("return_block_id: " + self.b_obj.find_block_id_from_canvas(
                                            return_block_id).__str__())
                                        print("return_block_id2: " + return_block_id.__str__())
                                        if iterated_block["B_type"]["block_inputTypes"][
                                            "inputBlockId"] == return_block_id:
                                            block_id = self.b_obj.find_block_id_from_canvas(k)
                                            current_block = self.b_obj.blocks[block_id]
                                            print("Das könnte Klappen!!!")
                                            dont_skip = True
                                            return block_id, current_block, dont_skip
                                            # return_block_id muss in Blocks gefunden werden und dahin gesprungen werden
                                            # dabei muss ein Block gefunden werden, der connected == True ah und als inputBlockId == return_block_id hat.
        print("-------END--------")
        return block_id, current_block, dont_skip

    def exec_evaluate_function(self, block_id):
        # print(block_id)
        block = self.b_obj.blocks[block_id]["B_type"]
        block_component_list = self.b_obj.blocks[block_id]["B_components"]
        func_name = block["func"]["func_name"]
        func_args = block["func"]["func_args"]
        func_arg_id_list = block["func"]["func_args_list"]
        is_pass_thorugh = block["func"]["isPassThrough"]
        # nextBlock = self.b_obj.blocks[nextBlock_id]["B_type"]
        self.b_obj.exec_obj = []
        if is_pass_thorugh:
            for i in range(block_component_list.__len__()):
                comp = block_component_list[i]
                if comp["entry"]:
                    comp_input_text = comp["entry"].get()  # Überprüfung ob es eine Variable ist.
                    if comp_input_text == "p":  # muss exception gefangen werden
                        comp_input_text = \
                        self.b_obj.blocks[block["block_inputTypes"]["inputBlockId"]]["B_type"]["block_outputTypes"][
                            "output_t"]
                        # print(comp_input_text)
                        converted = comp_input_text
                        self.b_obj.exec_obj.append(converted)
                    elif comp_input_text.__getitem__(0) == "$":  # comp_input_text.__getitem__(0) == "$"
                        if block["block_id"] == 2:
                            self.b_obj.exec_obj.append(self.g_var)
                            self.b_obj.exec_obj.append(dataTypes.BDString(comp_input_text))
                        else:
                            converted = self.g_var.get_value(comp_input_text)
                            self.b_obj.exec_obj.append(converted)
                    else:
                        converted = h_convert_to_data_types_from_string(comp_input_text)
                        if type(converted) == int:
                            self.b_obj.exec_obj.append(dataTypes.BDInteger(converted))
                        elif type(converted) == float:
                            self.b_obj.exec_obj.append(dataTypes.BDFloat(converted))
                        else:
                            self.b_obj.exec_obj.append(dataTypes.BDString(converted))
            data_type_obj = eval(self.exec_create_function_string_with_args(func_name))
            return data_type_obj
        else:
            for i in range(block_component_list.__len__()):
                comp = block_component_list[i]
                if comp["entry"]:
                    comp_input_text = comp["entry"].get()  # Überprüfung ob es eine Variable ist.
                    converted = h_convert_to_data_types_from_string(comp_input_text)
                    if comp_input_text.__getitem__(0) == "$":  # comp_input_text.__getitem__(0) == "$"
                        converted = self.g_var.get_value(comp_input_text)
                        self.b_obj.exec_obj.append(converted)
                    else:
                        if type(converted) == int:
                            self.b_obj.exec_obj.append(dataTypes.BDInteger(converted))
                        elif type(converted) == float:
                            self.b_obj.exec_obj.append(dataTypes.BDFloat(converted))
                        else:
                            self.b_obj.exec_obj.append(dataTypes.BDString(converted))
            data_type_obj = eval(self.exec_create_function_string_with_args(func_name))
            return data_type_obj

    # IDEE: das Objekt, welches als Text übergeben wird könnte auch gecastet werden.
    # IDEE: einfach direkten objektaufruf.
    #

    """        def exec_evaluateFunction(self, block_id):
        print(block_id)
        block = self.b_obj.blocks[block_id]["B_type"]
        blockComponentList = self.b_obj.blocks[block_id]["B_components"]
        funcName = block["func"]["func_name"]
        funcArgs = block["func"]["func_args"]
        funcArgIdList = block["func"]["func_args_list"]
        isPassThorugh = block["func"]["isPassThrough"]
        #nextBlock = self.b_obj.blocks[nextBlock_id]["B_type"]
        compInputText = ""
        alignedArgList = []
        if isPassThorugh:
            for i in range(blockComponentList.__len__()):
                comp = blockComponentList[i]
                if comp["entry"]:
                    compInputText = comp["entry"].get() #Überprüfung ob es eine Variable ist.
                    if compInputText == "p":
                        compInputText = self.b_obj.blocks[block["block_inputTypes"]["inputBlockId"]]["B_type"]["block_outputTypes"]["output_t"].__getstate__()
                        converted = compInputText
                        self.exec_obj.append(converted)
                    else:
                        converted = h_convertToDataTypesFromString(compInputText)
                        if type(converted) == int:
                            self.exec_obj.append(dataTypes.BDInteger(converted))
                        elif type(converted) == float:
                            self.exec_obj.append(dataTypes.BDFloat(converted))
                        else:
                            self.exec_obj.append(dataTypes.BDString(converted))
                    index = funcArgIdList.index(i)
                    alignedArgList.insert(index,  self.exec_obj[i])
            dataTypeObj = eval(self.exec_createFunctionStringWithArgs(funcName, alignedArgList))
            return dataTypeObj
        else:
            for i in range(blockComponentList.__len__()):
                comp = blockComponentList[i]
                if comp["entry"]:
                    compInputText = comp["entry"].get() #Überprüfung ob es eine Variable ist.
                    converted = h_convertToDataTypesFromString(compInputText)
                    if type(converted) == int:
                        self.exec_obj.append(dataTypes.BDInteger(converted))
                    elif type(converted) == float:
                        self.exec_obj.append(dataTypes.BDFloat(converted))
                    else:
                        self.exec_obj.append(dataTypes.BDString(converted))
                    index = funcArgIdList.index(i)
                    alignedArgList.insert(index, converted)
            dataTypeObj = eval(self.exec_createFunctionStringWithArgs(funcName, alignedArgList))
            return dataTypeObj"""

    def exec_create_function_string_with_args(self, func_name):
        out = "("
        for i in range(self.b_obj.exec_obj.__len__()):
            helper_string = "self.b_obj.exec_obj.__getitem__(" + i.__str__() + ")"
            out += helper_string
            if self.b_obj.exec_obj.__len__() - (i + 1) > 0:
                out += ","
        out += ")"
        print("self.b_obj." + func_name + out)
        return "self.b_obj." + func_name + out

    def exec_has_reached_end_of_script(self, block_id):
        if self.b_obj.blocks[block_id]["B_type"]["block_outputTypes"]["outputBlockId"]:
            return False
        else:
            return True

    def check_selected_tool(self):
        match self.selectedTool:
            case 0:
                print("no Tool Selected")
                return 1
            case 1:
                print("Move Tool (move a Block by selecting it and clicking on the Canvas)")
                return 2
            case 2:
                print(
                    "Link Tool (Links a Block to an other Block by selecting the first one and clicking on the second block)")
                return 3
            case 3:
                print("Delete Tool (deletes a Block by clicking on the Block)")
                return 4
        return 0

    def update_text_from_component(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        canvas_block_id = self.canvas.find_withtag(block_id)

        for i in range(block["B_components"].__len__()):
            canvas_component_id = block["B_components"][i]["id"]
            block_comp_dict = block["B_components"][i]["component"].get_data()
            canvas_edit_texts = self.canvas.find_withtag("EditText")
            for j in canvas_edit_texts:
                if j == canvas_component_id:
                    entry_item = block["B_components"].__getitem__(i)["entry"]
                    out = entry_item.get()
                    block["B_components"].__getitem__(i)["component"].set_text(out)
                    # print(block["B_components"].__getitem__(i)["component"].getData())

    def debug_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if item and "Block" in self.canvas.gettags(item)[0]:
            block_id = self.b_obj.find_block_id_from_canvas(item[0])
            self.update_text_from_component(block_id)

    def update_all_blocks_appearance(self):
        for i in self.canvas.find_withtag("Block"):
            block_id = self.b_obj.find_block_id_from_canvas(i)
            self.update_block_appearance(block_id)

    def update_block_appearance(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        canvas_block_id = self.canvas.find_withtag(self.b_obj.blocks[index]["B_type"]["id"])
        if canvas_block_id:
            if self.selectedBlockCanvasId:
                # print("Appearens: " + self.selectedBlockCanvasId.__str__() + canvas_block_id.__str__())
                if self.selectedBlockCanvasId == canvas_block_id[0]:
                    self.canvas.itemconfigure(self.selectedBlockCanvasId, outline="yellow", width=10)
                elif self.lastSelectedBlockCanvasId == canvas_block_id[0]:
                    self.canvas.itemconfigure(self.lastSelectedBlockCanvasId, outline="goldenrod", width=10)
                else:
                    outl = "black"
                    wdth = 1
                    dashed = ""
                    if block["B_type"]["connected"]:
                        if block["B_type"]["inLoop"]:
                            outl = "black"
                            wdth = 5
                            dashed = "."
                        else:
                            outl = "black"
                            wdth = 5
                            dashed = ""
                    else:
                        outl = "black"
                        wdth = 1
                        dashed = ""
                    self.canvas.itemconfigure(canvas_block_id[0], outline=outl, width=wdth, dash=dashed)

    def update_block_position(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        b_pos = self.b_obj.get_block_position(index)
        b_comp_length = block["B_components"].__len__()
        canvas_block_id = self.canvas.find_withtag(self.b_obj.blocks[index]["B_type"]["id"])
        # self.canvas.itemconfigure(canvas_block_id, x1=block["B_position"]["x1"], y1=block["B_position"]["y1"], x2=block["B_position"]["x2"], y2=block["B_position"]["y2"])
        # print("solte nur eine Zahl sein: " + canvas_block_id[0].__str__())
        self.canvas.moveto(canvas_block_id[0], block["B_position"]["x1"], block["B_position"]["y1"])

        for i in range(b_comp_length):
            component_type = None
            component_id = block["B_components"].__getitem__(i)["id"]
            canvas_id = self.canvas.find_withtag(component_id)
            comp_pos_x1, comp_pos_y1 = block["B_components"].__getitem__(i)["component"].get_position()
            actual_comp_pos_x, actual_comp_pos_y = self.canvas.coords(canvas_id)
            # dx, dy = h_getVectorBetweenPoints(b_pos["x1"], b_pos["y1"], comp_pos_x1, comp_pos_y1)
            # if (comp_pos_x1 + actual_comp_pos_x) != (b_pos["x1"] + dx) or (comp_pos_y1 + actual_comp_pos_y) != (b_pos["y1"] + dy):
            if block["B_components"].__getitem__(i)["component_id"] == 1:
                self.canvas.moveto(component_id, (comp_pos_x1 + b_pos["x1"] + 5), (comp_pos_y1 + b_pos["y1"] + 5))
            else:
                self.canvas.moveto(component_id, (comp_pos_x1 + b_pos["x1"]), (comp_pos_y1 + b_pos["y1"] - 5))
            # print("Components: " + comp_pos_x1.__str__() + " " + comp_pos_y1.__str__())
            # print(component_id)
            actual_comp_pos_x, actual_comp_pos_y = self.canvas.coords(canvas_id)
            # print("Components auf dem Canvas: " + actual_comp_pos_x.__str__() + " " + actual_comp_pos_y.__str__())

    def on_save_editor(self):
        def custom_serializer(obj):
            if isinstance(obj, dataTypes.BDInteger):
                return {"type": "BDInteger"}
            if isinstance(obj, dataTypes.BDFloat):
                return {"type": "BDFloat"}
            if isinstance(obj, dataTypes.BDString):
                return {"type": "BDString"}
            if isinstance(obj, block_components.TextView):
                return obj.get_data()
            if isinstance(obj, block_components.EditText):
                return obj.get_data()

            raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    json.dump(self.b_obj.blocks, file, default=custom_serializer, indent=4)
                messagebox.showinfo("Save Layout", "Layout saved successfully!")
            except Exception as e:
                messagebox.showerror("Save Error", f"An error occurred while saving: {e}")

    def on_load_editor(self):
        def custom_deserializer(obj):
            if isinstance(obj, dataTypes.BDInteger):
                return {"type": "BDInteger"}
            if isinstance(obj, dataTypes.BDFloat):
                return {"type": "BDFloat"}
            if isinstance(obj, dataTypes.BDString):
                return {"type": "BDString"}
            if isinstance(obj, block_components.TextView):
                return obj.get_data()
            if isinstance(obj, block_components.EditText):
                return obj.get_data()

            raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    loaded_data = json.load(file, object_hook=custom_deserializer)

            except Exception as e:
                messagebox.showerror("Load Error", f"An error occurred while loading: {e}")

    def debug_line(self, x1, y1, x2, y2):
        self.canvas.delete("debugLines")
        self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="debugLines")


if __name__ == "__main__":
    root = tk.Tk()
    window = BlockEditorView(root)
    root.mainloop()
