import graph
import image


class BDString:
    data = ""

    def __init__(self, text):
        self.data = text

    def __getstate__(self):
        return self.data


class BDInteger:
    data = 0

    def __init__(self):
        self.data = 1

    def add(self, num):
        self.data += num
        return self.data

    def toBDString(self):
        strg = BDString(self.data.__str__())
        return strg

    def __getstate__(self):
        return self.data


class BDDouble:
    data = 0.0

    def __init__(self):
        self.data = 1.0

    def __getstate__(self):
        return self.data


class BDImage:
    data = image.Image("assets/moeve.jpg")

    def __init__(self, file_path):
        self.data = image.Image(file_path)

    def __getstate__(self):
        return self.data


class BDGraph:
    data = graph.Graph([0], [0])

    def __init__(self, x, y):
        self.data = graph.Graph(x, y)

    def __getstate__(self):
        return self.data
