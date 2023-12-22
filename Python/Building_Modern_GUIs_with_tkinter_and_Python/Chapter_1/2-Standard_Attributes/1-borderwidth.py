from tkinter import *

# Create a Tk object and store it in the variable "myroot"
myroot = Tk()

# Create a Label object and store it in the variable "myl1"
# Pass myroot as master to myl1
# text: What the label displays
# bd: borderwidth (pixels)
# relief: How the label is outlined -> options: flat, groove, raised, ridge, solid, or sunken
myl1 = Label(myroot, text = 'Label1', bd = 1, relief = 'solid')

# pack myl1 onto the object passed to it (myroot).
myl1.pack()

# run the GUI
myroot.mainloop()