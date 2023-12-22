from tkinter import *
from tkinter import font
from tkinter.font import Font

# myobj_font = Font(options,...)
# Font options are:
    # 1.) family: What the font is named
    # 2.) size: The font height (integer value)
    # 3.) weight: The font thickness (bold or normal)
    # 4.) slant: Emphasis (italics or unslanted)
    # 5.) underline: Is the text underlined (Boolean: 1-underlined, 0-not underlined)
    # 6.) overstrike: Is the text struck-throught (Boolean: 1-strikethrough, 0-not strikethrough)

myroot = Tk()

myfont1 = Font(family='Terminal', size=12, weight='bold', slant='italic', underline=1, overstrike=1)

myl1 = Label(myroot, text='Python', font=myfont1)
myl1.pack()

# Create a list of fonts available on the machine running this code.
myfont_list = list(font.families())
for font in myfont_list:
    print(font,end= '\n')

myroot.mainloop()





