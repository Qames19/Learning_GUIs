from tkinter import *

root = Tk()
root.geometry('800x500')

# widget.grid(options**)
# options: column, columnspan, padx, pady, ipadx, ipady, row, rowspan, sticky
# 
# column: select the column the item will appear in (0 .. n, from left to right)
# columnspan: number of columns the item will encompass -> default 1
# padx: outside border padding (left/right)
# pady: outside border padding (up/down)
# ipadx: inside border padding (left/right)
# ipady: inside border padding (up/down)
# row: select the row the item will appear in (0 .. n, from up to down)
# rowspan: number of rows the item will encompass -> default 1
# sticky: where widget will stick if rowspan/columnspan is more than 1 (N,S,E,W,NE,NW,SE,SW) default -> NW

button1 = Button(root,
                 text   = 'Column 3')
button1.grid(column=3)

button2 = Button(root,
                 text   ="column2_span4")
button2.grid(column=2,columnspan=4)

button3 = Button(root,
                 text   = 'padx 7 from outside border')
button3.grid(row=2, padx=7)

button4 = Button(root,
                 text   = "pady 7 from outside border")
button4.grid(row=3, pady=7 )

button5 = Button(root,
                 text   = 'ipadx 7 from inside border')
button5.grid(row=4, ipadx=7)

button6 = Button(root,
                 text   = 'ipady 7 from inside border')
button6.grid(row=5, ipady=7)

button7 = Button(root,
                 text   = 'row 7')
button7.grid(row=7)

button8 = Button(root,
                 text   = 'row8_span3')
button8.grid(row=8,rowspan=3)

button9 = Button(root,
                 text   = 'I\'m very sticky')
button9.grid(columnspan=4,rowspan=4,sticky=SE)

root.mainloop()