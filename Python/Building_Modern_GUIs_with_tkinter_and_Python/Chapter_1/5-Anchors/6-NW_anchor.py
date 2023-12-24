from tkinter import *

root = Tk()

root.geometry('466x350')
label1 = Label(root, 
               text = 'Northwest Anchor', 
               anchor = NW, 
               font = ("Calibri", "21", "bold italic underline"), 
               bd = 10, 
               relief = 'sunken', 
               width = 18, 
               height = 5 )

label1.pack()
root.mainloop()