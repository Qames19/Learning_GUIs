from tkinter import *

root = Tk()
root.geometry('800x500')

# pack options: fill, expand, side

# fill: NONE, X, Y, BOTH -> default NONE
# expand: True or False. Expands widget when window expanded -> default 0
# side: TOP, BOTTOM, LEFT, RIGHT -> default TOP

button1 = Button(root,
                 text   = 'Top',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button1.pack(fill = None)

button2 = Button(root,
                 text   = 'X-fill',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button2.pack(fill = X, padx = 5, pady = 5)

button3 = Button(root,
                 text   = 'Right_Y-fill',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button3.pack(side = 'right', fill = Y, padx = 5, pady = 5)

button3_5 = Button(root,
                 text   = 'Left_Y-fill',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button3_5.pack(side = LEFT, fill = Y, padx = 5, pady = 5)

button4 = Button(root,
                 text   = 'Top_X-fill',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button4.pack(side = TOP, fill = X, padx = 5, pady = 5)

button5 = Button(root,
                 text   = 'Bottom_X-fill',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button5.pack(side = BOTTOM, fill = X, padx = 5, pady = 5)

button6 = Button(root,
                 text   = 'left_Both-fill_Expand',
                 fg     = 'Yellow',
                 bg     = 'Blue')
button6.pack(side = LEFT, fill = BOTH, expand = 1, padx = 5, pady = 5)

root.mainloop()