# globale Variablen, die vom BlockEditor erstellt wurden.

class Var:
    # data

    def __init__(self, value):
        self.data = value

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value


if __name__ == '__main__':
    v = Var("hello")
    print(v.getData())