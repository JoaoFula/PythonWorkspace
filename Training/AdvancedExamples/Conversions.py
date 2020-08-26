# This code will convert feet to meters.

from tkinter import *
from tkinter import ttk

# Define convertion equations
def feet2meters (*args):
    try:
        value = float(feet.get())
        meters.set("{:.2f}".format(float((0.3048 * value * 10000.0 + 0.5)/10000.0)))
    except ValueError:
        pass

def meters2feet (*args):
    try:
        value = float(meters.get())
        feet.set("{:.2f}".format(float(value*3.2808)))
    except ValueError:
        pass

def fahrenheit2celcius(*args):
    try:
        value = float(fahrenheit.get())
        celcius.set("{:.2f}".format(float((value-32)/1.8)))
    except ValueError:
        pass

def celcius2fahrenheit(*args):
    try:
        value = float(celcius.get())
        fahrenheit.set("{:.2f}".format(float((value*1.8)+32)))
    except ValueError:
        pass
    

# Define mainframe and String variables
root = Tk()
root.title("Conversions")
txt = Text(root, font=('Verdana',8))


mainframe = ttk.Frame(root, padding="25 25 120 120")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = DoubleVar()
feet.set('0.00')
meters = DoubleVar()
meters.set('0.00')
celcius = DoubleVar()
celcius.set('0.00')
fahrenheit = DoubleVar()
fahrenheit.set('0.00')

# Define interfaces and actions within interfaces
def FeetToMeters(*args):
    try:
        feetEntry = ttk.Entry(mainframe, width=7, textvariable=feet)
        feetEntry.grid(column=2, row=1, sticky=(W,E))
        
        ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
        ttk.Button(mainframe, text="Calculate", command=feet2meters).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="                    ").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="                     ").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)
       
   
        feetEntry.focus()
    except ValueError:
        pass

def MetersToFeet(*args):
    try:
        
        metersEntry = ttk.Entry(mainframe, width=7, textvariable=meters)
        metersEntry.grid(column=2, row=1, sticky=(W,E))

        ttk.Label(mainframe, textvariable=feet).grid(column=2, row=2, sticky=(W,E))
        ttk.Button(mainframe, text="Calculate", command=meters2feet).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="                      ").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="meters").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="                     ").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="feet").grid(column=3, row=2, sticky=W)
        metersEntry.focus()
    except ValueError:
        pass

def FahrenheitToCelcius(*args):
    try:
        fahrenheitEntry = ttk.Entry(mainframe, width=7, textvariable=fahrenheit)
        fahrenheitEntry.grid(column=2, row=1, sticky=(W,E))

        ttk.Label(mainframe, textvariable=celcius).grid(column=2, row=2, sticky=(W,E))
        ttk.Button(mainframe, text="Calculate", command=fahrenheit2celcius).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="                     ").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="fahrenheit").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="                     ").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="celcius").grid(column=3, row=2, sticky=W)
        fahrenheitEntry.focus()
    except ValueError:
        pass

def CelciusToFahrenheit(*args):
    try:
        
        celciusEntry = ttk.Entry(mainframe, width=7, textvariable=celcius)
        celciusEntry.grid(column=2, row=1, sticky=(W,E))

        ttk.Label(mainframe, textvariable=fahrenheit).grid(column=2, row=2, sticky=(W,E))
        ttk.Button(mainframe, text="Calculate", command=celcius2fahrenheit).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="                      ").grid(column=3, row=1, sticky=W) 
        ttk.Label(mainframe, text="celcius").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="                      ").grid(column=3, row=2, sticky=W)
        ttk.Label(mainframe, text="fahrenheit").grid(column=3, row=2, sticky=W)
        celciusEntry.focus()
    except ValueError:
        pass

# Define buttons that allow the change of conversion
ttk.Button(mainframe, text="Feet to Meters", command=FeetToMeters).grid(column=4, row=1, sticky=E)
ttk.Button(mainframe, text="Meters to Feet", command=MetersToFeet).grid(column=4, row=2, sticky=E)
ttk.Button(mainframe, text="Fahrenheit to Celcius", command=FahrenheitToCelcius).grid(column=5, row=1, sticky=E)
ttk.Button(mainframe, text="Celcius to Fahrenheit", command=CelciusToFahrenheit).grid(column=5, row=2, sticky=E)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


root.bind('<Return>', feet2meters)

root.mainloop()