import matplotlib.pyplot as gr
import pylab

def setGraph(x, y):
    gr.xlabel('x')
    gr.ylabel('y')
    gr.title('Your Graph')
    gr.grid(True)

    gr.plot(x, y, label="first")
    gr.legend()
    gr.show()


def getGraph():
    get_graph = gr.gca()


def modifyGraph(x,y, xlabel, ylabel, title, grid, label):
    x=x
    y=y
    gr.xlabel(xlabel if xlabel else "x")
    gr.ylabel(ylabel if ylabel else "y")
    gr.title(title if title else "Your Graph")
    if grid is not None:
        gr.grid(grid)
    gr.plot(x, y, label=label)
    gr.legend()
    gr.show()


#Bsp

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

setGraph(x,y)

h = [0, 1, 2, 3, 5]
b = [0, 3, 4, 9, 16]

modifyGraph(h,b, "humans", "time", "humanTime", True, "1990")

getGraph()
