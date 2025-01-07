import tkinter
from tkinter import ttk
from tkinter.colorchooser import askcolor
from tkinter import *

# Funktion und probefunktions
color = "red";


def clear():
    canvas.delete("all")
    canvas.create_rectangle(0, 0, 800, 500, fill="#729ecf")
    print("Canvas cleared")


def colorchooser():
    color = askcolor()[1]
    print(color)


def block1():
    print('block1')
    canvas.create_rectangle(0, 0, 80, 50, fill="red")


def block2():
    print('block2')
    canvas.create_rectangle(0, 0, 80, 50, fill="green")


def block3():
    print('block3')
    canvas.create_rectangle(0, 0, 80, 50, fill="blue")


def block4():
    print('block4')


def NewFile():
    print("New File!")


def OpenFile():
    print("open file")


def Blockeditor():
    button4.forget()
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)

    print("Block Editor")


def Dateneditor():
    button1.forget()
    button2.forget()
    button3.forget()
    button4.pack(side=LEFT)
    print("Daten Editor")


# Main window
fenster = Tk()

canvas = Canvas(fenster, width=800, height=500)
canvas.pack()
canvas.create_rectangle(0, 0, 800, 500, fill="#729ecf")

fenster.title("Layout")

# Menu
menu = Menu(fenster)
fenster.config(menu=menu, background="#729ecf")

# Reset Menu
remenu = Menu(menu)
remenu.configure(background="#6164e0")
menu.add_cascade(label="Reset", menu=remenu)
remenu.add_command(label="Exit", command=fenster.quit)
remenu.add_command(label="clear", command=clear)

# Dokumenten Menu
filemenu = Menu(menu)
filemenu.configure(background="#6164e0")
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)

# Editormenu
editormenu = Menu(menu)
editormenu.configure(background="#6164e0")
menu.add_cascade(label="Editor", menu=editormenu)
editormenu.add_command(label="Block editior", command=Blockeditor)
editormenu.add_command(label="Daten editior", command=Dateneditor)

# Buttons
button1 = Button(fenster, text="Block1", command=block1, background="#ee53ac")
button2 = Button(fenster, text="Block2", command=block2, background="#6ce160")
button3 = Button(fenster, text="Block3", command=block3, background="#e79d5a")
button4 = Button(fenster, text="Block4", command=block4, background="#408080")

exit_button = Button(fenster, text="Exit", command=fenster.quit, background="#d26f6f")
exit_button.pack(side=RIGHT)
color_button = Button(fenster, text="New Color", command=colorchooser, background="#6164e0")

color_button.pack()

fenster.mainloop()
