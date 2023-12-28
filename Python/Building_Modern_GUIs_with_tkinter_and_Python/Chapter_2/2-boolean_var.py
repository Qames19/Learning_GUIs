import tkinter as tk

root = tk.Tk()
root.geometry('800x500+750+35')
root.resizable(0,0)

use_option1 = tk.BooleanVar()
info_text = tk.StringVar()

def toggle_option1():
    if use_option1.get():
        info_text.set('Option1 is selected')
    else:
        info_text.set('Option1 is not selected')
    
check1 = tk.Checkbutton(root, variable=use_option1, font=('Calibri',12), text="Option1", command=toggle_option1)
check1.pack()

entry1 = tk.Entry(root, width=30, textvariable=info_text)
entry1.pack()
toggle_option1()

root.mainloop()