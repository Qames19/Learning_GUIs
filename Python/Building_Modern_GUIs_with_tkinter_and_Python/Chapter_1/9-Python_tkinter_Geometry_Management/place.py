from tkinter import *

root = Tk()
root.geometry('800x500')

# widget.place(options**)
# Options:      anchor, bordermode, relheight, relwidth, height, width, relx, rely, x, y

# anchor:       where widget is anchored: Compass Directions. default -> NW
# bordermode:   How is border included in coordinate system. INSIDE OUTSIDE. -> default INSIDE
# relheight:    percent value of parent objects height. Float value 0.0 - 1.0 
# relwidth:     percent value of parent objects width. Float value 0.0 - 1.0
# height:       height of widget in pixels. Integer value
# widht:        width of widget in pixels. Integer value
# relx:         x offset by percentage of parent. Float value 0.0 - 1.0
# rely:         y offxet by percentage of parent. Float value 0.0 - 1.0
# x:            x offset in pixels. Integer value
# y:            y offset in pixels. Integer value

button1 = Button(root,
                 text   = '75px tall')
button1.place(height=75, x=400, y=319)

button2 = Button(root,
                 text   = '85px wide')
button2.place(width=85, x = 350, y=132)

button3 = Button(root,
                 text   = 'relheight is 0.62')
button3.place(relheight=0.62)

button4 = Button(root,
                 text   = 'relwidth is 0.31')
button4.place(relwidth=0.31)

button5 = Button(root,
                 text   = 'relx is 0.48')
button5.place(relx=0.48)

button6 = Button(root,
                 text   = 'rely is 0.73')
button6.place(rely=0.73)

button7 = Button(root,
                 text   = 'x is 730')
button7.place(x=730)

button8 = Button(root,
                 text   = 'y is 410')
button8.place(y=410)

root.mainloop()