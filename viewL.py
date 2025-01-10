import tkinter as tk
from tkinter import *
import json
from tkinter import filedialog, messagebox


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

        self.testBlocks = {}

        self.blocks = {}  # Dictionary to store blocks with their IDs
        self.selected_block = None
        self.second_selected_block = None
        self.links = {}  # Dictionary to store linked blocks

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Button-2>", self.add_test_Block)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)

    def add_test_Block(self, event):
        # Create a green rectangle as the main block
        add_block = self.canvas.create_rectangle(100, 100, 200, 140, fill="green", tags="testBlock")
        self.testBlocks[add_block] = {
            "x1": 100, "y1": 100, "x2": 200, "y2": 140, "color": "green", "components": [],
            "entry_widget": None  # To store the associated Entry widget
        }

        # Create an Entry widget for editable text
        text_entry = tk.Entry(self.root, width=10)  # Width in characters
        text_entry.insert(0, "0")  # Default text
        entry_window = self.canvas.create_window(110, 110, window=text_entry, anchor="nw", tags="EditableText")

        # Store the Entry widget and its window ID
        self.testBlocks[add_block]["entry_widget"] = entry_window
        self.testBlocks[add_block]["components"].append({
            "component_id": entry_window,
            "type": "entry",
            "offsetX": 10,
            "offsetY": 10
        })

        # Add to the main blocks dictionary for unified handling
        self.blocks[add_block] = {
            "block_id": add_block,
            "entry_window": entry_window,
            "x1": 100, "y1": 100, "x2": 200, "y2": 140, "color": "green"
        }

    def add_block(self):
        block_id = self.canvas.create_rectangle(50, 50, 150, 150, fill="blue", tags="block")
        self.blocks[block_id] = {"x1": 50, "y1": 50, "x2": 150, "y2": 150, "color": "blue"}

    def add_link(self, block1, block2):
        if block1 not in self.links:
            self.links[block1] = []
        if block2 not in self.links[block1]:
            self.links[block1].append(block2)

        if block2 not in self.links:
            self.links[block2] = []
        if block1 not in self.links[block2]:
            self.links[block2].append(block1)

    def on_canvas_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if "testBlock" in self.canvas.gettags(item) or "block" in self.canvas.gettags(item):
            # Deselect the previous block
            if self.selected_block:
                self.canvas.itemconfigure(self.selected_block, fill=self.blocks[self.selected_block]["color"])

            # Select the new block
            self.selected_block = item[0]
            self.canvas.itemconfigure(self.selected_block, fill="lightblue")
        else:
            # Deselect if clicking outside blocks
            if self.selected_block:
                self.canvas.itemconfigure(self.selected_block, fill=self.blocks[self.selected_block]["color"])
            self.selected_block = None

    def on_canvas_drag(self, event):
        if self.selected_block:
            block = self.blocks[self.selected_block]
            dx = event.x - (block["x1"] + (block["x2"] - block["x1"]) // 2)
            dy = event.y - (block["y1"] + (block["y2"] - block["y1"]) // 2)

            # Move the rectangle
            self.canvas.move(self.selected_block, dx, dy)

            # Move the Entry widget
            if block["entry_window"]:
                self.canvas.move(block["entry_window"], dx, dy)

            # Update the block coordinates
            self.update_block_coords(self.selected_block)

            # Check for snapping
            self.check_snapping(event, self.selected_block)

    def check_snapping(self, event, block_id):
        current_coords = self.canvas.coords(block_id)
        current_x1, current_y1, current_x2, current_y2 = current_coords
        snapped = False
        for other_block_id, other_block in self.blocks.items():
            if other_block_id == block_id:  # Skip self
                continue

            other_coords = self.canvas.coords(other_block_id)
            other_x1, other_y1, other_x2, other_y2 = other_coords

            other_width = other_x2 - other_x1
            other_height = other_y2 - other_y1
            other_center_x = other_x1 + (other_x2 - other_x1) // 2
            other_center_y = other_y1 + (other_y2 - other_y1) // 2

            self.debug_line(abs((other_center_x + (other_width / 2)) - event.x),
                            abs((other_center_y + (other_height / 2)) - event.y), other_center_x, other_center_y)

            # self.debug_line(11, 11, 33, 33)

            if (abs((other_center_x + (other_width / 2)) - event.x) < 20 or abs(
                    (other_center_y + (other_height / 2)) - event.y) < 20
                    or abs((other_center_x - (other_width / 2)) + event.x) < 20 or abs(
                        (other_center_y - (other_height / 2)) + event.y) < 20):

                # Check proximity (snap threshold = 20 pixels)
                if abs(current_x2 - other_x1) < 20 or abs(current_x1 - other_x2) < 20 or \
                        abs(current_y2 - other_y1) < 20 or abs(current_y1 - other_y2) < 20:
                    # Highlight the block eligible for snapping
                    self.canvas.itemconfigure(other_block_id, outline="red", width=2)
                else:
                    self.canvas.itemconfigure(other_block_id, outline="", width=0)

                # Check proximity (snap threshold = 20 pixels)
                if abs(current_x2 - other_x1) < 20:  # Snap to the right side
                    dx = other_x1 - current_x2
                    dy = other_y1 - current_y1
                    snapped = True
                elif abs(current_x1 - other_x2) < 20:  # Snap to the left side
                    dx = other_x2 - current_x1
                    dy = other_y1 - current_y1
                    snapped = True
                elif abs(current_y2 - other_y1) < 20:  # Snap to the bottom
                    dx = other_x1 - current_x1
                    dy = other_y1 - current_y2
                    snapped = True
                elif abs(current_y1 - other_y2) < 20:  # Snap to the top
                    dx = other_x1 - current_x1
                    dy = other_y2 - current_y1
                    snapped = True
                else:
                    continue

            if snapped:
                # Move the rectangle
                self.canvas.move(block_id, dx, dy)

                # Move the associated Entry widget
                entry_window = self.blocks[block_id].get("entry_window")
                if entry_window:
                    self.canvas.move(entry_window, dx, dy)

                # Update block coordinates
                self.update_block_coords(block_id)

                # Add a link between the snapped blocks
                self.add_link(block_id, other_block_id)
                break

    def move_block(self, block_id, dx, dy, visited=None):
        if visited is None:
            visited = set()

        # Avoid circular movement
        if block_id in visited:
            return
        visited.add(block_id)

        # Move the block
        self.canvas.move(block_id, dx, dy)

        # Move the associated Entry widget
        entry_window = self.blocks[block_id].get("entry_window")
        if entry_window:
            self.canvas.move(entry_window, dx, dy)

        # Update coordinates
        self.update_block_coords(block_id)

        # Move linked blocks recursively
        for linked_block in self.links.get(block_id, []):
            self.move_block(linked_block, dx, dy, visited)

    def update_block_coords(self, block_id):
        coords = self.canvas.coords(block_id)
        self.blocks[block_id]["x1"], self.blocks[block_id]["y1"], self.blocks[block_id]["x2"], self.blocks[block_id][
            "y2"] = coords

    def delete_block(self):
        if self.selected_block:
            # Remove links associated with the block
            for linked_block in self.links.get(self.selected_block, []):
                self.links[linked_block].remove(self.selected_block)
            if self.selected_block in self.links:
                del self.links[self.selected_block]

            # Delete the block and its associated Entry widget
            self.canvas.delete(self.selected_block)
            entry_window = self.blocks[self.selected_block].get("entry_window")
            if entry_window:
                self.canvas.delete(entry_window)

            # Remove the block from the blocks dictionary
            del self.blocks[self.selected_block]
            self.selected_block = None

    def save_layout(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            data = {"blocks": self.blocks, "links": self.links}
            with open(file_path, "w") as file:
                json.dump(data, file)
            messagebox.showinfo("Save Layout", "Layout saved successfully!")

    def load_layout(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.blocks = data["blocks"]
                self.links = data.get("links", {})

            self.canvas.delete("all")
            for block_id, block in self.blocks.items():
                block_id = self.canvas.create_rectangle(
                    block["x1"], block["y1"], block["x2"], block["y2"], fill=block["color"], tags="block"
                )
                self.blocks[block_id] = block

                # Recreate Entry widget if it exists
                if "entry_widget" in block and block["entry_widget"]:
                    text_entry = tk.Entry(self.root, width=10)
                    text_entry.insert(0, block.get("text", ""))
                    entry_window = self.canvas.create_window(
                        block["x1"] + 10, block["y1"] + 10, window=text_entry, anchor="nw", tags="EditableText"
                    )
                    self.blocks[block_id]["entry_widget"] = entry_window

    def debug_line(self, x1, y1, x2, y2):
        self.canvas.delete("debugLines")
        self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="debugLines")


if __name__ == "__main__":
    root = tk.Tk()
    window = BlockEditorView(root)
    root.mainloop()