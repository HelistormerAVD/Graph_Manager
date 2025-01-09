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
        return self.text, self.fontColor, self.fontSize, self.width, self.height

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

    def __init__(self, text):
        self.text = text

    def getData(self):
        return self.text, self.fontColor, self.fontSize, self.width, self.height

    def getText(self):
        return self.text

    def setText(self, txt):
        self.text = txt



if __name__ == "__main__":
    tx = TextView("Hello World!")
