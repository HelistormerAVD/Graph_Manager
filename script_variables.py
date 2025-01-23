# globale Variablen, die vom BlockEditor erstellt wurden.

class Var:
    # data

    def __init__(self):
        self.data = []

    def insert_value(self, var_name, data):
        for i in range(self.data.__len__()):
            if self.data[i]["name"] == var_name:
                self.data.insert(i, {"name": var_name, "data": data})
        else:
            self.data.append({"name": var_name, "data": data})

    def get_value(self, var_name):
        for i in range(self.data.__len__()):
            if self.data[i]["name"] == var_name:
                return self.data[i]["data"]

    def set_value(self, var_name, value):
        for i in range(self.data.__len__()):
            if self.data[i]["name"] == var_name:
                self.data[i]["data"] = value


if __name__ == '__main__':
    v = Var()
    v.insert_value("test", 1)
    v.insert_value("neu", "hallo")
    print(v.get_value("test"))
