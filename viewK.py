import tkinter as tk
from tkinter import *
import json
import block
from tkinter import filedialog, messagebox

import block_components
from util import h_getNextEmptyDictionary


class BlockEditorView:
    b_obj = block.Block()

    def __init__(self, root):
        self.root = root
        self.root.title("Block-Based Graphical Editor")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(root, bg="lightgray")
        self.toolbar.pack(fill=tk.X)

        self.add_block_button = tk.Button(self.toolbar, text="Math Operations", command=self.add_block)
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.editorObjects = {"widget" : None, "Id" : None, "type" : str, "components" : []}

        #self.canvas.bind("<Button-1>", self.on_canvas_click)
        #self.canvas.bind("<Button-2>", self.add_test_Block)
        #self.canvas.bind("<B1-Motion>", self.on_canvas_drag)


    def add_block(self):

        indexOfCanvasObject = h_getNextEmptyDictionary(self.editorObjects)

        index = self.b_obj.initBlock_add()
        newBlock = self.b_obj.blocks[index]
        b_comp_length = newBlock["B_components"].__len__()
        #print(newBlock["B_components"])
        self.editorObjects[indexOfCanvasObject]["Id"] = self.canvas.create_rectangle(newBlock["B_position"]["x1"],
                                     newBlock["B_position"]["y1"],
                                     newBlock["B_position"]["x2"],
                                     newBlock["B_position"]["y2"],
                                     fill=newBlock["B_type"]["color"],
                                     tags="Integer_add")
        self.editorObjects[indexOfCanvasObject]["type"] = "Rect"
        for i in range(b_comp_length):
            componentType = None
            componentId = newBlock["B_components"].__getitem__(i)["id"]
            match componentId:
                case 0:
                    textViewSettings = newBlock["B_components"].__getitem__(i)["component"].getData()
                    componentType = tk.Entry(self.root, width=textViewSettings["width"])
                    componentType.insert(i, textViewSettings["text"])
                    textViewComp = self.canvas.create_window(textViewSettings["x1"] + newBlock["B_position"]["x1"],
                                                             textViewSettings["y1"] + newBlock["B_position"]["y1"],
                                                             window=componentType,
                                                             anchor="nw",
                                                             tags="TextView")
                    self.editorObjects[indexOfCanvasObject]["components"].append({"Id" : textViewComp, "type" : "TextView"})
                case 1:
                    editTextSettings = newBlock["B_components"].__getitem__(i)["component"].getData()
                    componentType = tk.Entry(self.root, width=editTextSettings["width"])
                    componentType.insert(i, editTextSettings["text"])
                    editTextComp = self.canvas.create_window(editTextSettings["x1"] + newBlock["B_position"]["x1"],
                                                             editTextSettings["y1"] + newBlock["B_position"]["y1"],
                                                             window=componentType,
                                                             anchor="nw",
                                                             tags="EditText")
                    self.editorObjects[indexOfCanvasObject]["components"].append({"Id" : editTextComp, "type" : "EditText"})

    def updateBlockPosition(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        b_pos = block.getBlockPosition(index)
        b_comp_length = block["B_components"].__len__()

        newPosX = block["B_position"]["x1"]
        newPosY = block["B_position"]["y1"]
        

        self.canvas.__getitem__()
        self.canvas.move()

        for i in range(b_comp_length):
            componentType = None
            componentId = block["B_components"].__getitem__(i)["id"]
            match componentId:
                case 0:
                    componentType = None
                    print("err")
                case 1:
                    self.canvas.move()
                    editTextSettings = block["B_components"].__getitem__(i)["component"].getData()


    def debug_line(self, x1, y1, x2, y2):
        self.canvas.delete("debugLines")
        self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="debugLines")


if __name__ == "__main__":
    root = tk.Tk()
    window = BlockEditorView(root)
    root.mainloop()