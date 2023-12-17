from tkinter import *

myroot=Tk()

# width and height adjust the width and height surrounding label
# underline can only be used once to underline a single character (0 based index of text)
# font can be used to underline all of text if given a font with underline
myl1=Label(myroot, text='Python', width=20, height=5, underline=1, font=('Calibri', 15))
myl1.pack()

myroot.mainloop()