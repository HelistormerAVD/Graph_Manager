# globale Variablen, die vom BlockEditor erstellt wurden.

class Var:
    # data

    def __init__(self):
        self.data = []

    def insert_value(self, varName, data):
        for i in range(self.data.__len__()):
            if self.data[i]["name"] == varName:
                self.data.insert(i, {"name" : varName, "data" : data})
        else:
            self.data.append({"name" : varName, "data" : data})

    def get_value(self, varName):
        for i in range(self.data.__len__()):
            if self.data[i]["name"] == varName:
                return self.data[i]["data"]

    def set_value(self, varName, value):
        for i in range(self.data.__len__()):
            if self.data[i]["name"] == varName:
                self.data[i]["data"] = value


if __name__ == '__main__':
    v = Var()
    v.insert_value("test", 1)
    v.insert_value("neu", "hallo")
    print(v.get_value("test"))