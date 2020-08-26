# Create a message box

from tkinter import *

master = Tk()

whateverYouDo = "Welcome to Python. Python is awesome!"
msg = Message(master, text=whateverYouDo)

msg.config(bg="white", font=("Verdana", 22, "italic"))

msg.pack()
mainloop()

# Create an image box with profile image

from tkinter import *

canvasWidth = 225
canvasHeight = 225

master = Tk()

canvas = Canvas(master,
            width = canvasWidth,
            height = canvasHeight)

canvas.pack()

img = PhotoImage(file="AdvancedExamples/Python.PNG")
canvas.create_image(20, 20, anchor=NW, image=img)

mainloop()

# Draw by dragging mouse

from tkinter import *
from tkinter import ttk

lastx, lasty = 0,0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky = (N,W,E,S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

root.mainloop()
