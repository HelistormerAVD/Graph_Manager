import tkinter as tk
from tkinter import filedialog, messagebox
import json

class TextView:

    text = "textView"

    def __init__(self, text):
        self.text = text


if __name__ == "__main__":
    tx = TextView("Hello World!")
