# globale Variablen, die vom BlockEditor erstellt wurden.

class Var:
    # data

    def __init__(self, value):
        self.data = value

    def get_value(self):
        return self.data

    def set_value(self, value):
        self.data = value


if __name__ == '__main__':
    v = Var("hello")
    print(v.get_value())