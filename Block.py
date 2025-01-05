

class Block:

    #FIXED VARIABLES
    BLOCK_ID = 0
    BLOCK_POS_X = 0
    BLOCK_POS_Y = 0
    BLOCK_WIDTH = 20
    BLOCK_HEIGHT = 20

    #LOKAL VARIABLES
    B_layout = {}
    B_color = None
    B_inputTypes = {}
    B_outputTypes = {}
    

    def __init__(self):
        self.BLOCK_ID = 0

    def initBlock_add(self):
        self.BLOCK_ID = 1
        self.BLOCK_POS_X = 10
        self.BLOCK_POS_Y = 10
        self.BLOCK_WIDTH = 20
        self.BLOCK_HEIGHT = 20




if __name__ == "__main__":
    Block()
