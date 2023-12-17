from tkinter import *

myroot = Tk() # create variable myroot and assign it to be a default object of the Tk class

myroot.resizable(width = True, height = False) # width is adjustable, but height is not 
### NOTE: This does not appear to work on wsl ###

myroot.mainloop() # kick off the mainloop of the Tk class stored in myroot

print("tkinter window has been closed") # this message is printed to the terminal when myroot is closed