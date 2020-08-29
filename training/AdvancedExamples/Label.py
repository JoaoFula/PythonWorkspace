from tkinter import *
canvasWidth = 100
canvasHeight = 50

class App:
    def __init__(self, 
                master, 
                width = canvasWidth, 
                height = canvasHeight):
        # Define the frame
        frame = Frame(master, 
                    width = canvasWidth, 
                    height = canvasHeight)

        frame.pack()
        #Define the buttons, one closes and one runs the writeSlogan function
        self.button = Button(frame,
                            text="Close",
                            fg="Red",
                            command = frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame,
                            text = "Click Me!",
                            fg = "blue",
                            command = self.writeSlogan)
        self.slogan.pack(side=LEFT)
        
        self.button.config(height = 2,
                        width = 20)
        
        self.slogan.config(height = 2,
                        width = 20)
                
    def writeSlogan(self):
        print("Welcome to Portugal")

root = Tk()
root.title("Hello world")
app = App(root)
root.mainloop()

# This code is for the timer

import tkinter as tk
counter = 0
def counterLabel(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000,count)   #when timer exceeds 1000
    count()
# rerun count until the stop button is pressed and root is destroyed. label after runs an error in this moment 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counterLabel(label)
button = tk.Button(root, 
                text="Stop", 
                width = 35,
                command = root.destroy)
button.pack()
root.mainloop()