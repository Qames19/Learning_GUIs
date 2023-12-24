from tkinter import *

root = Tk()

root.geometry('800x600')


button1 = Button(root,
                 text = 'FLAT',
                 font = ('Times-New-Roman', 14),
                 relief = 'flat',
                 bd = 5)
button1.pack()

button2 = Button(root,
                 text = 'RAISED',
                 font = ('Times-New-Roman', 14),
                 relief = 'raised',
                 bd = 5)
button2.pack()

button3 = Button(root,
                 text = 'GROOVE',
                 font = ('Times-New-Roman', 14),
                 relief = 'groove',
                 bd = 5)
button3.pack()

button4 = Button(root,
                 text = 'SUNKEN',
                 font = ('Times-New-Roman', 14),
                 relief = 'sunken',
                 bd = 5)
button4.pack()

button5 = Button(root,
                 text = 'RIDGE',
                 font = ('Times-New-Roman', 14),
                 relief = 'ridge',
                 bd = 5)
button5.pack()

button6 = Button(root,
                 text = "SOLID",
                 font = ('Times-New-Roman', 14),
                 relief = 'solid',
                 bd = 5)
button6.pack()

root.mainloop()