import tkinter as tk
from tkinter import *
import json
import block
from tkinter import filedialog, messagebox

import block_components


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

        #self.canvas.bind("<Button-1>", self.on_canvas_click)
        #self.canvas.bind("<Button-2>", self.add_test_Block)
        #self.canvas.bind("<B1-Motion>", self.on_canvas_drag)


    def add_block(self):
        index = self.b_obj.initBlock_add()
        newBlock = self.b_obj.blocks[index]
        b_length = newBlock["B_components"].__len__()
        self.canvas.create_rectangle(newBlock["B_position"]["x1"],
                                     newBlock["B_position"]["y1"],
                                     newBlock["B_position"]["x2"],
                                     newBlock["B_position"]["y2"],
                                     fill=newBlock["B_type"]["color"],
                                     tags="Integer_add")
        for i in range(b_length):
            componentType = None
            componentId = newBlock["B_components"]["id"]
            match componentId:
                case 0:
                    componentType = None
                case 1:
                    editTextSettings = newBlock["B_components"]["component"].getData()
                    componentType = tk.Entry(self.root, width=editTextSettings["width"])
                    componentType.insert(0, editTextSettings["text"])
                    editTextComp = self.canvas.create_window(editTextSettings["x1"] + newBlock["B_position"]["x1"],
                                                             editTextSettings["y1"] + newBlock["B_position"]["y1"],
                                                             window=componentType,
                                                             anchor="nw",
                                                             tags="EditText")


    def debug_line(self, x1, y1, x2, y2):
        self.canvas.delete("debugLines")
        self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="debugLines")


if __name__ == "__main__":
    root = tk.Tk()
    window = BlockEditorView(root)
    root.mainloop()