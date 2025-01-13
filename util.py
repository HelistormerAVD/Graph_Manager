# nützliche Hilfs-Funktionen.

def h_getNextEmptyDictionary(dictionary):
    a = dictionary.items().__len__()
    b = 0
    if a == 0:
        return 0
    for i in range(a):
        #print(a)
        b = i
        if not dictionary.get(i):
            return b
    return b + 1

def h_findFromCanvasDictObj(canvasObjId, dictionary, isComponent):
    length = dictionary.__len__()



if __name__ == "__main__":
    print("Test einer Hilfs-Funktion")
    #------------------

    werte = {}
    werte[0] = {"test" : True, "zahl" : 1, "vals" : {}}
    werte[1] = {"test": True, "zahl": 1, "vals": {}}
    werte[2] = {"test": True, "zahl": 1, "vals": {}}
    #werte[3] = {"test": True, "zahl": 1, "vals": {}}
    #werte[4] = {"test": True, "zahl": 1, "vals": {}}
    #werte[5] = {"test": True, "zahl": 1, "vals": {}}
    #werte[6] = {"test": True, "zahl": 1, "vals": {}}
    out = h_getNextEmptyDictionary(werte)
    print(out)