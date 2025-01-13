import tkinter as tk
from tkinter import filedialog, messagebox
import json

# Just a normal Text to be displayed
class TextView:
    text = "textView"
    fontColor = "gray"
    fontSize = 10
    width = 20
    height = 14

    def __init__(self, text):
        self.text = text


    def getData(self):
        return {
            "text": self.text,
            "fontColor": self.fontColor,
            "fontSize": self.fontSize,
            "width": self.width,
            "height": self.height
        }

    def getText(self):
        return self.text

    def setText(self, txt):
        self.text = txt


# Editable Text Box
class EditText:
    text = "EditText"
    fontColor = "black"
    fontSize = 10
    width = 20
    height = 14
    isOnlyNumber = False
    x = 0
    y = 0

    def __init__(self, text):
        self.text = text

    def getData(self):
        return {
            "text": self.text,
            "fontColor": self.fontColor,
            "fontSize": self.fontSize,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def getText(self):
        return self.text

    def setText(self, txt):
        self.text = txt

    def getPosition(self):
        return self.x, self.y

    def changePosition(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

if __name__ == "__main__":
    tx = TextView("Hello World!")
    et = EditText("Editable")
    print(tx.getData())
    print(et.getData())
    et.changePosition(100, 200)
    print("New Position:", et.getPosition())
