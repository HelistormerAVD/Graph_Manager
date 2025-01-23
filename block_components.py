import tkinter as tk
from tkinter import filedialog, messagebox
import json


# Just a normal Text to be displayed
class TextView:

    """ """

    def __init__(self):
        self.component_Id = 0
        self.canvas_Id = None
        self.x1 = 0
        self.y1 = 0
        self.text = "TextView"
        self.fontColor = "black"
        self.width = 20

    def get_data(self):
        return {"id": self.component_Id,
                "canvas_id": self.canvas_Id,
                "x1": self.x1,
                "y1": self.y1,
                "text": self.text,
                "fontColor": self.fontColor,
                "width": self.width}

    def set_data(self, component_id: int, x1: int, y1: int, text: str, font_color: str, width: int):
        self.component_Id = component_id
        self.x1 = x1
        self.y1 = y1
        self.text = text
        self.fontColor = font_color
        self.width = width

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt

    def set_position(self, pos_x, pos_y):
        self.x1 = pos_x
        self.y1 = pos_y

    def get_position(self):
        return self.x1, self.y1


# Editable Text Box
class EditText:
    isOnlyNumber = False

    def __init__(self):
        self.component_Id = 0
        self.canvas_Id = None
        self.x1 = 0
        self.y1 = 0
        self.text = "EditText"
        self.width = 20

    def set_data(self, component_id: int, x1: int, y1: int, text: str, width: int):
        self.component_Id = component_id
        self.canvas_Id = None
        self.x1 = x1
        self.y1 = y1
        self.text = text
        self.width = width

    def get_data(self):
        return {"id": self.component_Id,
                "canvas_id": self.canvas_Id,
                "x1": self.x1,
                "y1": self.y1,
                "text": self.text,
                "width": self.width}

    def get_text(self):
        return self.text

    def set_text(self, txt):
        self.text = txt

    def set_position(self, pos_x, pos_y):
        self.x1 = pos_x
        self.y1 = pos_y

    def get_position(self):
        return self.x1, self.y1

    def check_if_only_number(self):
        checked = str.isdigit(self.text)
        if checked:
            return 1
        else:
            return 0


if __name__ == "__main__":
    tx = TextView("Hello World!")
