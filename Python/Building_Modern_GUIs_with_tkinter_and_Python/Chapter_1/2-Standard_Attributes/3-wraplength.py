from tkinter import *

myroot=Tk()

# wraplength is amount of pixels allowed before wrapping text to next line
myl1=Label(myroot, text= 'Python', wraplength=2)
myl1.pack()

# wraplenght 0 is do not wrap
myl2=Label(myroot, text= 'awesome', wraplength=0)
myl2.pack()

myroot.mainloop()