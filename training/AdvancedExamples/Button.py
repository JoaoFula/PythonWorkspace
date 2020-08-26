import tkinter
from tkinter import ttk

#Create the button
root = tkinter.Tk()
style = ttk.Style()

#defines the style for C.TButton
style.map("C.TButton",
        foreground = [('pressed','red'), ('active', 'blue')],
        background = [('pressed', '!disabled', 'black'), ('active', 'white')]
        )

coloredBtn = ttk.Button(text = "Click me!", style="C.TButton").pack()

#mainloop
root.mainloop()
