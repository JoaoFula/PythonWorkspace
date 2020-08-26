# This code will create some rectangles and some other things
from tkinter import *

canvasWidth = 300
canvasHeight = 200

colours=("#476042", "yellow")
box = []

for ratio in (0.2, 0.35):
    box.append((canvasWidth * ratio,
                canvasHeight * ratio,
                canvasWidth * (1-ratio),
                canvasHeight * (1-ratio)))

master = Tk()

#create a couple of rectangles
w = Canvas(master, width=200, height = 100)
w.pack()


# w.create_rectangle(left edge X, top edge Y, right edge X, bottom edge Y, colour to fill) 
# where (0,0) is the top left corner of the window
w.create_rectangle(50, 20, 150, 80, fill="#ccff33")
w.create_rectangle(65, 35, 135, 65, fill="#ff0000")
w.create_line(0, 0, 50, 20, fill="#ff0000", width=3)
w.create_line(0, 100, 50, 80, fill="#ff0000", width=3)
w.create_line(150, 20, 200, 0, fill="#ff0000", width=3)
w.create_line(150, 80, 200, 100, fill="#ff0000", width=3)

#modify top code
w = Canvas(master, 
            width = canvasWidth, 
            height = canvasHeight)

w.pack()

for i in range(2):
    w.create_rectangle(box[i][0], box[i][1], box[i][2], box[i][3], fill=colours[i])
w.create_line(0,
            0,
            box[0][0],
            box[0][1],
            fill = colours[0],
            width = 5)
w.create_line(0,
            canvasHeight,
            box[0][0],
            box[0][3],
            fill = colours[0],
            width = 5)
w.create_line(box[0][2],
            box[0][1],
            canvasWidth,
            0,
            fill = colours[0],
            width = 8)
w.create_line(box[0][2],
            box[0][3],
            canvasWidth,
            canvasHeight,
            fill = colours[0],
            width = 5)

w.create_text(canvasWidth/2,
            canvasHeight/2,
            text="Close to Paint")
mainloop() 