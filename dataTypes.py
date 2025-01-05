import graph
import image


class BDString:

    data = ""

    def __init__(self):
        self.data = "Hello World!"


class BDInteger:

    data = 0

    def __init__(self):
        self.data = 0


class BDDouble:

    data = 0.0

    def __init__(self):
        self.data = 0.0


class BDImage:

    data = image.Image("assets/moeve.jpg")

    def __init__(self, file_path):
        self.data = image.Image(file_path)


class BDGraph:

    data = graph.Graph([0], [0])

    def __init__(self, x , y):
        self.data = graph.Graph(x, y)