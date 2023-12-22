from tkinter import *
from tkinter import ttk

myroot = Tk()

# grid places the widget on the stage in a grid layout by 0 indexed row x column
myb1 = Button(myroot, text='Without Highlight Thickness')
myb1.grid(row=0, column=1)

# highlightthickness puts padding between the text and the button border
# padx provides extra space in the x direction (outside of button)
# pady provides extra space in the y direction (outside of button)
myb2 = Button(myroot, text='With Highlight Thickness', highlightthickness=10)
myb2.grid(row=1, column=1, padx=10, pady=10)

myroot.mainloop()