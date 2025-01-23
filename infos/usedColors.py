import tkinter as tk
from time import sleep


# !!! NICHT FÜRS PROJEKT ZUM AUSFÜHREN !!!

# Hier stehen die Farben, die von den einzelnen Blöcken verwendet werden.
# Bitte keine Farben für Blöcke Benutzen, die von elementaren/wichtigen Blöcken (wie StartBlock = Grün und EndBlock = Rot) verwendet werden.
# Stattdessen sollen "größere Kontraste" zu diesen Farben erzeugt werden.
# -> (man kann z.B. auch Dunkel Grün oder Hell Grün nehmen, jedoch sollte man einen klaren Unteschied zu den Blöcken erkennen können.)
# Zudem sollten Blöcke nach Datentypen/Kategorie entsprechend gefärbt sein. (z.B. alle Blöcke die mit Integern Arbeiten = blau)


# ---------------------------------Farb Palette--------------------------------------
""" 
    ein neuer Block kann wie folgt hinzugefügt werden:
    
    self.colorsForBlocks[<neue ID>] = {"blockName" : "<BlockName>", "color" : "<name>", "outline" : None}

    Der Outline by Blöcken (sofern nötig) soll die Farbe passend zum Datentyp der Ausgabe vom Block anzeigen. (um es Benutzer-freundlicher zu machen)
    Bei Blöcken die keinen Outline haben (bzw. Standard = Schwarz), soll dieser nur mit der breite 1 angezeigt werden.
    Wenn ein Block sich in einer Schleife befindet, soll dieser eine gestrichelte outline besitzen. (um es Benutzer-freundlicher zu machen)

"""
# -----------------------------------------------------------------------------------

class FarbPalette:

    def __init__(self, root):
        self.root = root
        self.root.title("Block-Based Graphical Editor")

        self.canvas = tk.Canvas(root, bg="white", width=1080, height=720)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.toolbar = tk.Frame(root, bg="lightgray")
        self.toolbar.pack(fill=tk.X)

        self.colorsForBlocks = {} # {"blockName" : "BlockName", "color" : "name", "outline" : None}
        self.positions = {} # {"x1": 50, "y1": 50, "x2": 150, "y2": 150}
        self.positionsLable = {}  # {"x1": 50, "y1": 50, "x2": 150, "y2": 150}

        self.colors(root)
        self.setPositions()

    def colors(self, r):
        self.colorsForBlocks[0] = {"blockName" : "StartBlock", "color" : "green2", "outline" : None}
        self.colorsForBlocks[1] = {"blockName" : "EndBlock", "color" : "red", "outline" : None}
        self.colorsForBlocks[2] = {"blockName" : "SetVariable", "color" : "orange red", "outline" : None}
        self.colorsForBlocks[3] = {"blockName" : "Int_add", "color" : "dodger blue", "outline" : None}
        self.colorsForBlocks[4] = {"blockName" : "Int_sub", "color" : "dodger blue", "outline" : None}
        self.colorsForBlocks[5] = {"blockName" : "Int_mult", "color" : "dodger blue", "outline" : None}
        self.colorsForBlocks[6] = {"blockName" : "Int_div", "color" : "dodger blue", "outline" : None}
        self.colorsForBlocks[7] = {"blockName": "float_add", "color": "royal blue", "outline": None}
        self.colorsForBlocks[8] = {"blockName": "float_sub", "color": "royal blue", "outline": None}
        self.colorsForBlocks[9] = {"blockName": "float_mult", "color": "royal blue", "outline": None}
        self.colorsForBlocks[10] = {"blockName": "float_div", "color": "royal blue", "outline": None}
        self.colorsForBlocks[11] = {"blockName": "str_concat", "color": "deep pink", "outline": "black"}
        self.colorsForBlocks[12] = {"blockName": "str_subDiv", "color": "deep pink", "outline": "black"}
        self.colorsForBlocks[13] = {"blockName": "str_trim", "color": "deep pink", "outline": "black"}
        self.colorsForBlocks[14] = {"blockName": "str_split", "color": "deep pink", "outline": "black"}
        self.colorsForBlocks[15] = {"blockName": "str_find", "color": "deep pink", "outline": "black"}
        self.colorsForBlocks[16] = {"blockName": "List_Insert", "color": "mediumpurple", "outline": None}
        self.colorsForBlocks[17] = {"blockName": "List_get", "color": "mediumpurple", "outline": None}
        self.colorsForBlocks[18] = {"blockName": "List_delete", "color": "mediumpurple", "outline": None}
        self.colorsForBlocks[19] = {"blockName": "List_sort", "color": "mediumpurple", "outline": None}
        self.colorsForBlocks[20] = {"blockName": "Graph_Set", "color": "khaki2", "outline": None}
        self.colorsForBlocks[21] = {"blockName": "Graph_Get", "color": "khaki2", "outline": None}
        self.colorsForBlocks[22] = {"blockName": "Graph_Modify", "color": "khaki2", "outline": None}
        self.colorsForBlocks[23] = {"blockName": "Function", "color": "teal", "outline": None}
        self.colorsForBlocks[24] = {"blockName": "Goto", "color": "teal", "outline": None}
        self.colorsForBlocks[25] = {"blockName": "Return Function", "color": "teal", "outline": None}
        self.colorsForBlocks[26] = {"blockName": "If", "color": "orange", "outline": None}
        self.colorsForBlocks[27] = {"blockName": "WhileLoop", "color": "orange", "outline": None}
        self.colorsForBlocks[28] = {"blockName": "WhileLoop_end", "color": "orange", "outline": None}
        self.colorsForBlocks[29] = {"blockName": "Nop", "color": "gray50", "outline": None}
        self.colorsForBlocks[30] = {"blockName": "loadFileInList", "color": "salmon4", "outline": None}





    def setPositions(self):
        wert = 10
        rows = wert
        cols = self.colorsForBlocks.__len__() // wert
        length = self.colorsForBlocks.__len__()
        if (length % wert) > 0:
            cols += 1
        count = 0
        for i in range(cols):
            for j in range(rows):
                if length > count:
                    self.positions[count] = {"x1": (j * 100) + 10, "y1": (i * 100) + 10, "x2": (j * 100) + 80, "y2": (i * 100) + 80}
                    self.positionsLable[count] = {"x": self.positions[count]["x1"] + 35, "y": self.positions[count]["y1"] + 35}
                    self.drawColors(count)
                    count += 1

    def drawColors(self, count):
        outl = None
        wth = 0
        dashed = ""
        if self.colorsForBlocks[count]["outline"]:
            outl = self.colorsForBlocks[count]["outline"]
            wth = 5
            if count == 11 or count == 12:
                dashed = "" # dashed = "."
        else :
            outl = self.colorsForBlocks[count]["outline"]
            wth = 1

        blockObj = self.canvas.create_rectangle(self.positions[count]["x1"],
                                     self.positions[count]["y1"],
                                     self.positions[count]["x2"],
                                     self.positions[count]["y2"],
                                     fill=self.colorsForBlocks[count]["color"],
                                     outline=outl,
                                     width=wth,
                                     dash=dashed)
        blockTxt = self.canvas.create_text(self.positionsLable[count]["x"],
                                self.positionsLable[count]["y"],
                                text=self.colorsForBlocks[count]["blockName"],
                                width="100",
                                fill="black",
                                tags="txt",
                                justify="left")






if __name__ == "__main__":
    root = tk.Tk()
    window = FarbPalette(root)
    root.mainloop()