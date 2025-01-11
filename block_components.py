import tkinter as tk
from tkinter import filedialog, messagebox
import json


# Just a normal Text to be displayed
class TextView:

    def __init__(self, component_id, posX, posY, text):
        self.component_Id = component_id
        self.x1 = posX
        self.y1 = posY
        self.text = text
        self.fontSize = 10
        self.fontColor = "black"
        self.width = 20
        self.height = 14


    def getData(self):
        return {"id" : self.component_Id,
                "x1" : self.x1,
                "y1" : self.y1,
                "text" : self.text,
                "fontSize" : self.fontSize,
                "fontColor" : self.fontColor,
                "width" : self.width,
                "height" : self.height}

    def getText(self):
        return self.text

    def setText(self, txt):
        self.text = txt

    def setPosition(self, posX, posY):
        self.x1 = posX
        self.y1 = posY

    def getPosition(self):
        return self.x1, self.y1


# Editable Text Box
class EditText:
    isOnlyNumber = False

    def __init__(self, component_id, posX, posY, text):
        self.component_Id = component_id
        self.x1 = posX
        self.y1 = posY
        self.text = text
        self.fontSize = 10
        self.fontColor = "black"
        self.width = 20
        self.height = 14

    def getData(self):
        return {"id": self.component_Id,
                "x1": self.x1,
                "y1": self.y1,
                "text": self.text,
                "fontSize": self.fontSize,
                "fontColor": self.fontColor,
                "width": self.width,
                "height": self.height}

    def getText(self):
        return self.text

    def setText(self, txt):
        self.text = txt

    def setPosition(self, posX, posY):
        self.x1 = posX
        self.y1 = posY

    def getPosition(self):
        return self.x1, self.y1

    def checkIfOnlyNumber(self):
        checked = str.isdigit(self.text)
        if checked:
            return 1
        else:
            return 0


if __name__ == "__main__":
    tx = TextView("Hello World!")
