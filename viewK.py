import tkinter as tk
from tkinter import *
import json
import block
from tkinter import filedialog, messagebox

import block_components
from util import h_getNextEmptyDictionary, h_getVectorBetweenPoints


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

        #self.editorObjects = {}
        self.selectedTool = 1
        self.selectedBlock = None

        #self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Button-2>", self.onCanvasClick)
        self.canvas.bind("e", self.onCanvasClick)
        #self.canvas.bind("<B1-Motion>", self.on_canvas_drag)


    def add_block(self):

        index = self.b_obj.initBlock_add()
        newBlock = self.b_obj.blocks[index]
        b_comp_length = newBlock["B_components"].__len__()
        #print(newBlock["B_components"])
        newBlock["B_type"]["id"] = self.canvas.create_rectangle(newBlock["B_position"]["x1"],
                                     newBlock["B_position"]["y1"],
                                     newBlock["B_position"]["x2"],
                                     newBlock["B_position"]["y2"],
                                     fill=newBlock["B_type"]["color"],
                                     tags=["Block", "Integer_add"])
        for i in range(b_comp_length):
            componentType = None
            componentId = newBlock["B_components"].__getitem__(i)["component_id"]
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
                    newBlock["B_components"].__getitem__(i)["id"] = textViewComp
                    #self.b_obj.editorObjects[indexOfCanvasObject]["components"].append({"Id" : textViewComp, "type" : "TextView"})
                case 1:
                    editTextSettings = newBlock["B_components"].__getitem__(i)["component"].getData()
                    componentType = tk.Entry(self.root, width=editTextSettings["width"])
                    componentType.insert(i, editTextSettings["text"])
                    editTextComp = self.canvas.create_window(editTextSettings["x1"] + newBlock["B_position"]["x1"],
                                                             editTextSettings["y1"] + newBlock["B_position"]["y1"],
                                                             window=componentType,
                                                             anchor="nw",
                                                             tags="EditText")
                    #self.b_obj.editorObjects[indexOfCanvasObject]["components"].append({"Id" : editTextComp, "type" : "EditText"})
                    newBlock["B_components"].__getitem__(i)["id"] = editTextComp
                    #newBlock["B_components"][componentId]["id"] = editTextComp
                    print(newBlock)

    def onCanvasClick(self, event):
        if self.selectedBlock:
            item = self.canvas.find_closest(event.x, event.y)
            if item and "Block" in self.canvas.gettags(item)[0]:
                if self.checkSelectedTool() == 1:
                    block_id = self.b_obj.findBlockIdFromCanvas(item[0])
                if self.checkSelectedTool() == 2:
                    block_id = self.b_obj.findBlockIdFromCanvas(item[0])
                    self.b_obj.moveBlock(block_id, event.x, event.y)
                    self.updateBlockPosition(block_id)
                if self.checkSelectedTool() == 3:
                    block_id = self.b_obj.findBlockIdFromCanvas(item[0])
                    self.onCreateLink(block_id, self.selectedBlock)
                if self.checkSelectedTool() == 4:
                    block_id = self.b_obj.findBlockIdFromCanvas(item[0])
                    self.onDeleteBlock(block_id, self.selectedBlock)
                else:
                    print("nothing to Do")
        else:
            item = self.canvas.find_closest(event.x, event.y)
            if item and "Block" in self.canvas.gettags(item)[0]:
                self.selectedBlock = item

    def onCreateLink(self, block_id, selected_block_id):
        print("create a link between two blocks")
        # überprüfe, ob block_id == selected_block_id (darf nicht die selbe sein)
        #   in block-dict vom selected_block_id füge "inputBlockId" = block_id
        #   in block-dict vom selected_block_id füge "input_t" = dataTypes vom block_id "output_t"
        #   in block-dict vom block_id füge "outputBlockId" = selected_block_id
        #   in block-dict vom block_id setze "connected" = True
        #   in block-dict vom selected_block_id setze "connected" = True
        #   funktion moveBlock(aus b_obj) mit selected_block_id an x1 von block_id und (y2 von block_id) + Blockhöhe (40)
        print("eingefügt")

    def onDeleteBlock(self, block_id, selected_block_id):
        print("deletes a block from the Canvas and from block-dict. (self.b_obj.blocks[index])")
        # überprüfe, od es der Startblock ist (der darf nicht gelöscht werden)
        # überprüfe, ob block_id == selected_block_id
        #   lösche block_id vom Canvas
        #   lösche block_id vom block-dict.
        #   setze self.selectedBlock auf None
        # ansonsten print("fehler")
        print("deleted")

    def onExecuteScript(self):
        print("Executes the final script build by the Block Editor")
        """ Variablen für die Funktion: """
        # startBlock_id: finde die ID des Startblocks in b_obj.blocks
        # nextBlock_id: finde die nächste block_id vom Block, welcher als "outputBlockId" im StartBlock-dict. gespeichert ist.
        # functionName: <speichert die Funktion als name, die von einem Block ausgeführt werden soll.> Anfangs str
        # functionArgs: <speichert die Args für die function, welche von einem Block ausgeführt werden soll. Wird als dataTypes gespeichert.> Anfangs None
        # f_executeEnd: Flag, wenn das ende der verlinkten Blöcke erreicht wurde.
        # f_executeBreak: Flag, wenn die exeution abgebrochen werden muss, falls es z.B. einen Fehler gibt.
        # f_executesuccess: Flag, wenn execution geklappt hat.
        """-----------------------------"""


        # finde die
        print("Executed")

    def checkSelectedTool(self):
        match self.selectedTool:
            case 0:
                print("no Tool Selected")
                return 1
            case 1:
                print("Move Tool (move a Block by selecting it and clicking on the Canvas)")
                return 2
            case 2:
                print("Link Tool (Links a Block to an other Block by selecting the first one and clicking on the second block)")
                return 3
            case 3:
                print("Delete Tool (deletes a Block by clicking on the Block)")
                return 4
        return 0





    def updateBlockPosition(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        b_pos = self.b_obj.getBlockPosition(index)
        b_comp_length = block["B_components"].__len__()
        canvasBlock_id = self.canvas.find_withtag(block_id)
        self.canvas.move(canvasBlock_id, block["B_position"]["x1"], block["B_position"]["y1"])


        for i in range(b_comp_length):
            componentType = None
            componentId = block["B_components"].__getitem__(i)["id"]
            canvas_id = self.canvas.find_withtag(componentId)
            compPosX1, compPosY1 = block["B_components"].__getitem__(i)["component"].getPosition()
            actualCompPosX, actualCompPosY = self.canvas.coords(canvas_id)
            dx, dy = h_getVectorBetweenPoints(b_pos["x1"], b_pos["y1"], compPosX1, compPosY1)
            if (compPosX1 + actualCompPosX) != (b_pos["x1"] + dx) or (compPosY1 + actualCompPosY) != (b_pos["y1"] + dy):
                self.canvas.move(componentId, compPosX1, compPosY1)


    def debug_line(self, x1, y1, x2, y2):
        self.canvas.delete("debugLines")
        self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="debugLines")



if __name__ == "__main__":
    root = tk.Tk()
    window = BlockEditorView(root)
    root.mainloop()