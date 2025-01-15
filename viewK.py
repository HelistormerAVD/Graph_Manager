import tkinter as tk
from tkinter import *
import json
import block
from tkinter import filedialog, messagebox

import block_components
from script_variables import Var
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

        self.add_block_button = tk.Button(self.toolbar, text="Select", command=lambda: self.switchEditorTool(0))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Add Block", command=self.add_block)
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Move", command=lambda: self.switchEditorTool(1))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Link", command=lambda: self.switchEditorTool(2))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.add_block_button = tk.Button(self.toolbar, text="Delete", command=lambda: self.switchEditorTool(3))
        self.add_block_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.selectedTool = 1

        self.selectedBlockItem = None
        self.selectedBlockId = None
        self.selectedBlockCanvasId = None

        self.lastSelectedBlockItem = None
        self.lastSelectedBlockId = None
        self.lastSelectedBlockCanvasId = None

        #self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<Button-2>", self.onCanvasClick)
        self.canvas.bind("<Button-3>", self.debugClick)
        #self.canvas.bind("<B1-Motion>", self.on_canvas_drag)


    def add_block(self):

        index = self.b_obj.initBlock_Integer_add()
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
                    textViewComp = self.canvas.create_text(textViewSettings["x1"] + newBlock["B_position"]["x1"],
                                                             textViewSettings["y1"] + newBlock["B_position"]["y1"], text=textViewSettings["text"], fill=textViewSettings["fontColor"], tags="TextView", font=('Helvetica', '12'))
                    newBlock["B_components"].__getitem__(i)["id"] = textViewComp
                    #self.b_obj.editorObjects[indexOfCanvasObject]["components"].append({"Id" : textViewComp, "type" : "TextView"})
                case 1:
                    editTextSettings = newBlock["B_components"].__getitem__(i)["component"].getData()
                    componentType = tk.Entry(self.root, width=editTextSettings["width"])
                    componentType.insert(0, editTextSettings["text"])
                    editTextComp = self.canvas.create_window(editTextSettings["x1"] + newBlock["B_position"]["x1"],
                                                             editTextSettings["y1"] + newBlock["B_position"]["y1"],
                                                             window=componentType,
                                                             anchor="nw",
                                                             tags="EditText")
                    #self.b_obj.editorObjects[indexOfCanvasObject]["components"].append({"Id" : editTextComp, "type" : "EditText"})
                    newBlock["B_components"].__getitem__(i)["id"] = editTextComp
                    newBlock["B_components"].__getitem__(i)["entry"] = componentType

                    #newBlock["B_components"][componentId]["id"] = editTextComp
                    print(newBlock)

    def switchEditorTool(self, toolNumber):
        if toolNumber < 0 or toolNumber > 3:
            print("wrong tool to be selected")
        else:
            self.selectedTool = toolNumber

    def setSelectedBlock(self, event):
        item = self.canvas.find_closest(event.x, event.y, start="Block")
        if item:
            if self.selectedBlockItem:
                self.lastSelectedBlockItem = self.selectedBlockItem
                self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                self.lastSelectedBlockId = self.selectedBlockId
                self.selectedBlockItem = item
                self.selectedBlockCanvasId = item[0]
                self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                return 1
            else:
                if self.selectedBlockItem != self.lastSelectedBlockItem:
                    self.lastSelectedBlockItem = self.selectedBlockItem
                    self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                    self.lastSelectedBlockId = self.selectedBlockId
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.lastSelectedBlockItem = self.selectedBlockItem
                    self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                    self.lastSelectedBlockId = self.selectedBlockId
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
        else:
            print("err")
            return 0

    def checkDualSelection(self):
        if self.selectedBlockItem and self.lastSelectedBlockItem:
            return 1
        else:
            return 0

    def checkDualSelectionIsSame(self):
        if self.selectedBlockId == self.lastSelectedBlockId:
            return 1
        else:
            return 0

    """
        if self.selectedBlockItem:
            if self.lastSelectedBlockItem:
                if item:
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.selectedBlockItem = None
                    self.selectedBlockCanvasId = None
                    self.selectedBlockId = None
                    return 0
            else:
                if item:
                    self.lastSelectedBlockItem = self.selectedBlockItem
                    self.lastSelectedBlockCanvasId = self.selectedBlockCanvasId
                    self.lastSelectedBlockId = self.selectedBlockId
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.selectedBlockItem = None
                    self.selectedBlockCanvasId = None
                    self.selectedBlockId = None
                    return 0
        else:
            if self.lastSelectedBlockItem:
                if item:
                    self.selectedBlockItem = self.lastSelectedBlockItem
                    self.selectedBlockCanvasId = self.lastSelectedBlockCanvasId
                    self.selectedBlockId = self.lastSelectedBlockId
                    self.lastSelectedBlockItem = None
                    self.lastSelectedBlockId = None
                    self.lastSelectedBlockCanvasId = None
                    return 1
                else:
                    self.selectedBlockItem = self.lastSelectedBlockItem
                    self.selectedBlockCanvasId = self.lastSelectedBlockCanvasId
                    self.selectedBlockId = self.lastSelectedBlockId
                    self.lastSelectedBlockItem = None
                    self.lastSelectedBlockId = None
                    self.lastSelectedBlockCanvasId = None
                    return 0
            else:
                if item:
                    self.selectedBlockItem = item
                    self.selectedBlockCanvasId = item[0]
                    self.selectedBlockId = self.b_obj.findBlockIdFromCanvas(item[0])
                    return 1
                else:
                    self.selectedBlockItem = None
                    self.selectedBlockCanvasId = None
                    self.selectedBlockId = None
                    return 0
    """

    # cur last item : Block Ausgewählt | Letzter Ausgewählter Block | nächster Ausgewählter Block
    #   0   0   0   : nein, nein, nein -> alles auf None setzen.
    #   0   0   1   : es gibt einen Block aber es wurde noch nichts ausgewählt -> nur current = item
    #   0   1   0   : keinen aktuellen Block, es gab einen Block, aber keinen neuer -> alles auf None (da wir nicht wissen, ob der Block noch existiert)
    #   0   1   1   : keinen selected Block, es gab einen Block, und es gibt einen neuen -> current = item, last = None (da wir nicht wissen, ob der Block noch existiert)
    #   1   0   0   : ausgewählter block, kein letzten, kein neuer -> last = current, current = None
    #   1   0   1   : ausgewählter block, kein letzten, aber neuer -> last = current, current = item
    #   1   1   0   : ausgewählter block, es gibt einen letzten, kein neuer -> nichts
    #   1   1   1   : ausgewählter block, es gibt einen letzten, und einen neuen -> last = current, current = item




    def onCanvasClick(self, event):
        match self.checkSelectedTool():
            case 1:
                block_id = self.selectedBlockId
                self.setSelectedBlock(event)
                self.updateAllBlocksAppearance()
            case 2:
                if self.selectedBlockItem:
                    block_id = self.selectedBlockId
                    self.b_obj.moveBlock(block_id, event.x, event.y)
                    self.updateBlockPosition(block_id)
                    #self.updateBlockAppearance(block_id)
                    self.updateAllBlocksAppearance()
                else:
                    print("no Block Selected")
            case 3:
                if self.selectedBlockItem:
                    self.onCreateLink(self.selectedBlockId, self.lastSelectedBlockId)
                else:
                    print("no Block Selected")
            case 4:
                if self.selectedBlockItem:
                    block_id = self.selectedBlockId
                    self.onDeleteBlock(block_id, self.selectedBlockItem)
                else:
                    print("no Block Selected")

    def onCreateLink(self, block_id, selected_block_id):
        """ erstellt einen Link zwischen den beiden Blöcken mit den block_ids block_id und selected_block_id """
        print("create a link between two blocks")
        if not self.checkDualSelectionIsSame():
            print(block_id)
            print(selected_block_id)
            if block_id != None and selected_block_id != None:

                #blockItems = self.canvas.gettags(selected_block_id)
                blockItems = self.selectedBlockItem
                blockItems2 = self.lastSelectedBlockItem
                print(blockItems, blockItems2)


                block_dict = self.b_obj.blocks[block_id]["B_type"]
                selected_block_dict = self.b_obj.blocks[selected_block_id]["B_type"]

                selected_block_dict["block_inputTypes"]["input_t"] = block_dict["block_outputTypes"]["output_t"]
                selected_block_dict["block_inputTypes"]["inputBlockId"] = block_dict["block_outputTypes"]["outputBlockId"]
                selected_block_dict["connected"] = True

                block_dict["block_outputTypes"]["outputBlockId"] = selected_block_id
                block_dict["connected"] = True

                block_height = self.b_obj.blockHeight
                pos = self.b_obj.getBlockPosition(block_id)

                x1 = pos["x1"] # 10 da jede umrandung die hälfte nach innen und außen ist
                y1 = pos["y1"] + block_height

                self.b_obj.moveBlock(selected_block_id, x1, y1)
                self.updateBlockPosition(selected_block_id)
                self.updateAllBlocksAppearance()
                print("link created")
        else:
            print(f"block_id {block_id} and selected_block_id {selected_block_id} must not be equal")
        # überprüfe, ob block_id == selected_block_id (darf nicht die selbe sein)
        #   in block-dict vom selected_block_id füge "inputBlockId" = block_id
        #   in block-dict vom selected_block_id füge "input_t" = dataTypes vom block_id "output_t"
        #   in block-dict vom block_id füge "outputBlockId" = selected_block_id
        #   in block-dict vom block_id setze "connected" = True
        #   in block-dict vom selected_block_id setze "connected" = True
        #   funktion moveBlock(aus b_obj) mit selected_block_id an x1 von block_id und (y2 von block_id) + Blockhöhe (40)

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


    def updateTextFromComponent(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        canvasBlock_id = self.canvas.find_withtag(block_id)

        for i in range(block["B_components"].__len__()):
            canvasComponent_id = block["B_components"][i]["id"]
            block_comp_dict = block["B_components"][i]["component"].getData()
            canvasEditTexts = self.canvas.find_withtag("EditText")
            for j in canvasEditTexts:
                if j == canvasComponent_id:
                    entryItem = block["B_components"].__getitem__(i)["entry"]
                    out = entryItem.get()
                    block["B_components"].__getitem__(i)["component"].setText(out)
                    #print(block["B_components"].__getitem__(i)["component"].getData())

    def debugClick(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        if item and "Block" in self.canvas.gettags(item)[0]:
            block_id = self.b_obj.findBlockIdFromCanvas(item[0])
            self.updateTextFromComponent(block_id)

    def updateAllBlocksAppearance(self):
        for i in self.canvas.find_withtag("Block"):
            block_id = self.b_obj.findBlockIdFromCanvas(i)
            self.updateBlockAppearance(block_id)



    def updateBlockAppearance(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        canvasBlock_id = self.canvas.find_withtag(self.b_obj.blocks[index]["B_type"]["id"])
        if canvasBlock_id:
            if self.selectedBlockCanvasId:
                #print("Appearens: " + self.selectedBlockCanvasId.__str__() + canvasBlock_id.__str__())
                if self.selectedBlockCanvasId == canvasBlock_id[0]:
                    self.canvas.itemconfigure(self.selectedBlockCanvasId, outline="yellow", width=10)
                else:
                    outl = "black"
                    wdth = 1
                    dashed = ""
                    if block["B_type"]["connected"]:
                        if block["B_type"]["inLoop"]:
                            outl = "black"
                            wdth = 5
                            dashed = "."
                        else:
                            outl = "black"
                            wdth = 5
                            dashed = ""
                    else:
                        outl = "black"
                        wdth = 1
                        dashed = ""
                    self.canvas.itemconfigure(canvasBlock_id[0], outline=outl, width=wdth, dash=dashed)




    def updateBlockPosition(self, block_id):
        index = block_id
        block = self.b_obj.blocks[index]
        b_pos = self.b_obj.getBlockPosition(index)
        b_comp_length = block["B_components"].__len__()
        canvasBlock_id = self.canvas.find_withtag(self.b_obj.blocks[index]["B_type"]["id"])
        #self.canvas.itemconfigure(canvasBlock_id, x1=block["B_position"]["x1"], y1=block["B_position"]["y1"], x2=block["B_position"]["x2"], y2=block["B_position"]["y2"])
        #print("solte nur eine Zahl sein: " + canvasBlock_id[0].__str__())
        self.canvas.moveto(canvasBlock_id[0], block["B_position"]["x1"], block["B_position"]["y1"])


        for i in range(b_comp_length):
            componentType = None
            componentId = block["B_components"].__getitem__(i)["id"]
            canvas_id = self.canvas.find_withtag(componentId)
            compPosX1, compPosY1 = block["B_components"].__getitem__(i)["component"].getPosition()
            actualCompPosX, actualCompPosY = self.canvas.coords(canvas_id)
            #dx, dy = h_getVectorBetweenPoints(b_pos["x1"], b_pos["y1"], compPosX1, compPosY1)
            #if (compPosX1 + actualCompPosX) != (b_pos["x1"] + dx) or (compPosY1 + actualCompPosY) != (b_pos["y1"] + dy):
            if block["B_components"].__getitem__(i)["component_id"] == 1:
                self.canvas.moveto(componentId, (compPosX1 + b_pos["x1"] + 5), (compPosY1 + b_pos["y1"] + 5))
            else:
                self.canvas.moveto(componentId, (compPosX1 + b_pos["x1"]), (compPosY1 + b_pos["y1"] - 5))
            #print("Components: " + compPosX1.__str__() + " " + compPosY1.__str__())
            #print(componentId)
            actualCompPosX, actualCompPosY = self.canvas.coords(canvas_id)
            #print("Components auf dem Canvas: " + actualCompPosX.__str__() + " " + actualCompPosY.__str__())


    def debug_line(self, x1, y1, x2, y2):
        self.canvas.delete("debugLines")
        self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="debugLines")



if __name__ == "__main__":
    root = tk.Tk()
    window = BlockEditorView(root)
    root.mainloop()