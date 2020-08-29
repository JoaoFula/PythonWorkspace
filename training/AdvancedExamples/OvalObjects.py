# Creating oval objects or shapes

from tkinter import *

canvasWidth = 400
canvasHeight = 400
pythonGreen = "#476042"

def polygon_star(canvas, x, y, p, t, outline = pythonGreen, fill = 'yellow', width = 1):
    points = []
    for i in (1,-1):
        points.extend((x, y + i*p))
        points.extend((x + i*t, y + i*t))
        points.extend((x + i*p, y))
        points.extend((x + i*t, y - i*t))

    print(points)

    canvas.create_polygon(points, outline = outline, fill=fill, width = width)

master = Tk()

w = Canvas(master,
        width = canvasWidth,
        height = canvasHeight)

w.pack()

p = 50
t = 15

nsteps = 10
stepX = int(canvasWidth/nsteps)
stepY = int(canvasHeight/nsteps)

for i in range(1, nsteps):
    polygon_star(w, i*stepX, i*stepY, p, t, outline = "red", fill = 'green', width = 3)
    polygon_star(w, i*stepX, canvasHeight - i*stepY, p, t, outline = "red", fill = 'green', width = 3)

mainloop()


# oval objects widgets

from tkinter import *

def checkered(canvas, lineDistance):
    for x in range(lineDistance, canvasWidth, lineDistance):
        canvas.create_line(x, 0, x, canvasHeight, fill = '#476042')
    for y in range(lineDistance, canvasHeight, lineDistance):
        canvas.create_line(0, y, canvasWidth, y, fill = '#476042')

master = Tk()

canvasWidth = 200
canvasHeight = 200

w = Canvas(master,
        width = canvasWidth,
        height = canvasHeight)

w.pack()

checkered(w,10 )

mainloop()

from tkinter import *

canvasWidth = 300
canvasHeight = 80  

master = Tk()

canvas = Canvas(master, width = canvasWidth, height = canvasHeight )

canvas.pack()

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead"]
nsteps = len(bitmaps)
stepX = int(canvasWidth/nsteps)

for i in range(0, nsteps):
    canvas.create_bitmap((i+1)*stepX-stepX/2, 50, bitmap = bitmaps[i])

mainloop()