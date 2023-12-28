from tkinter import *

root = Tk()
root.geometry('800x500+500+100')
root.resizable(0,0)

var1 = StringVar()
entry1 = Entry(root, font = ('Arial', 14), textvariable=var1)
entry1.pack()

def show_var1():
    data1 = var1.get()
    print(data1)
    var1.set('')

button1 = Button(root, font = ('Arial', 14), text='Print to Terminal', command=show_var1)
button1.pack()

root.mainloop()