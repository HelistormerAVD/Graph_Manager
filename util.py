# nützliche Hilfs-Funktionen.
import dataTypes


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

def h_getVectorBetweenPoints(x1, y1, x2, y2):
    return (x2 - x1), (y2 - y1)

def h_findFromCanvasDictObj(canvasObjId, dictionary, isComponent):
    length = dictionary.__len__()

def h_convertToDataTypesFromString(inputString : str):
    if str.isdigit(inputString):
        if inputString.find(".") > -1:
            return float(inputString)
        else:
            return int(inputString)
    else:
        return inputString
    # noch checken ob "[" enthalten -> dann Liste

def h_convert_str_to_datatypes(input_string : str):
    if input_string == "dataTypes.BDInteger":
        return dataTypes.BDInteger(0)
    elif input_string == "dataTypes.BDFloat":
        return dataTypes.BDFloat()
    elif input_string == "dataTypes.BDString":
        return dataTypes.BDString()
    elif input_string == "dataTypes.BDList":
        return dataTypes.BDList()
    elif input_string == "dataTypes.BDGraph":
        return dataTypes.BDGraph()
    else:
        return None



if __name__ == "__main__":
    print("Test einer Hilfs-Funktion")
    #------------------

    werte = {}
    werte[0] = {"test" : True, "zahl" : 1, "vals" : {}}
    werte[1] = {"test": True, "zahl": 1, "vals": {}}
    werte[2] = {"test": True, "zahl": 1, "vals": {}}
    werte[3] = {"test": True, "zahl": 1, "vals": {}}
    werte[4] = {"test": True, "zahl": 1, "vals": {}}
    #werte[5] = {"test": True, "zahl": 1, "vals": {}}
    #werte[6] = {"test": True, "zahl": 1, "vals": {}}
    out = h_getNextEmptyDictionary(werte)
    print(out)