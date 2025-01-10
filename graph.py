import matplotlib.pyplot as plt


class Graph:
    pointsX = []
    pointsY = []
    graph = plt

    def __init__(self, x, y):
        self.pointsX = x
        self.pointsY = y

    def setGraph(self):
        self.graph.xlabel('x')
        self.graph.ylabel('y')
        self.graph.title('Your Graph')
        self.graph.grid(True)

        self.graph.plot(self.pointsX, self.pointsY, label="first")
        self.graph.legend()
        self.graph.show()

    def getGraph(self):
        get_graph = self.graph.gca()
        return get_graph

    def modifyGraph(self, x, y, xlabel, ylabel, title, grid, label):
        self.pointsX = x
        self.pointsY = y
        self.graph.xlabel(xlabel if xlabel else "x")
        self.graph.ylabel(ylabel if ylabel else "y")
        self.graph.title(title if title else "Your Graph")
        if grid is not None:
            self.graph.grid(grid)
        self.graph.plot(self.pointsX, self.pointsY, label=label)
        self.graph.legend()
        self.graph.show()


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]
    myGraph = Graph(x, y)
    myGraph.setGraph()
    h = [0, 1, 2, 3, 5]
    b = [0, 3, 4, 9, 16]
    myGraph.modifyGraph(h, b, "humans", "time", "humanTime", True, "1990")
    myGraph.getGraph()
