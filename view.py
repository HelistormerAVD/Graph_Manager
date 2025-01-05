import tkinter as tk
from tkinter import filedialog, messagebox
import json

from fontTools.unicodedata import block
from numpy.ma.core import filled


class BlockEditorView:

    def __init__(self, root):
        self.root = root
        self.root.title("Block-Based Graphical Editor")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(root, bg="lightgray")
        self.toolbar.pack(fill=tk.X)

        self.add_block_button = tk.Button(self.toolbar, text="Math Operations", command=self.add_block)
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_layout)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.load_button = tk.Button(self.toolbar, text="Load", command=self.load_layout)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.delete_button = tk.Button(self.toolbar, text="Delete Block", command=self.delete_block)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.blocks = {}  # Dictionary to store blocks with their IDs
        self.selected_block = None
        self.second_selected_block = None

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)


    def add_block(self):
        block_id = self.canvas.create_rectangle(50, 50, 150, 150, fill="blue", tags="block")
        self.blocks[block_id] = {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}


    def on_canvas_click(self, event):
        for block_id in self.blocks.items():
            if self.selected_block != self.canvas.find("all"):
                self.canvas.itemconfigure(block_id, fill="blue")
        item = self.canvas.find_closest(event.x, event.y)
        if "block" in self.canvas.gettags(item):
            self.selected_block = item[0]
            if self.selected_block:
                self.canvas.itemconfigure(self.selected_block, fill="lightblue")
        else:
            self.selected_block = None


    def on_canvas_drag(self, event):
        if self.selected_block:
            block = self.blocks[self.selected_block]
            dx = event.x - (block["x1"] + (block["x2"] - block["x1"]) // 2)
            dy = event.y - (block["y1"] + (block["y2"] - block["y1"]) // 2)
            self.canvas.move(self.selected_block, dx, dy)
            self.update_block_coords(self.selected_block)


    def update_block_coords(self, block_id):
        coords = self.canvas.coords(block_id)
        self.blocks[block_id]["x1"], self.blocks[block_id]["y1"], self.blocks[block_id]["x2"], self.blocks[block_id][
            "y2"] = coords


    def delete_block(self):
        if self.selected_block:
            self.canvas.delete(self.selected_block)
            del self.blocks[self.selected_block]
            self.selected_block = None


    def save_layout(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as file:
                json.dump(self.blocks, file)
            messagebox.showinfo("Save Layout", "Layout saved successfully!")


    def load_layout(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as file:
                self.blocks = json.load(file)
            self.canvas.delete("all")
            for block_id, block in self.blocks.items():
                block_id = self.canvas.create_rectangle(
                    block["x1"], block["y1"], block["x2"], block["y2"], fill=block["color"], tags="block"
                )
                self.blocks[block_id] = block

if __name__ == "__main__":
    root = tk.Tk()
    editor = BlockEditorView(root)
    root.mainloop()