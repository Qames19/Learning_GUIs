from tkinter import *

myroot = Tk() # create variable myroot and assign it to be a default object of the Tk class
### https://docs.python.org/3.11/library/tkinter.html
# class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
#   Construct a toplevel Tk widget, which is usually the main window of an application, and initialize a Tcl interpreter for this widget. Each instance has its own associated Tcl interpreter.
#   The Tk class is typically instantiated using all default values. However, the following keyword arguments are currently recognized:
# screenName
#   When given (as a string), sets the DISPLAY environment variable. (X11 only)
# baseName
#   Name of the profile file. By default, baseName is derived from the program name (sys.argv[0]).
# className
#   Name of the widget class. Used as a profile file and also as the name with which Tcl is invoked (argv0 in interp).
# useTk
#   If True, initialize the Tk subsystem. The tkinter.Tcl() function sets this to False.
# sync
#   If True, execute all X server commands synchronously, so that errors are reported immediately. Can be used for debugging. (X11 only)
# use
#   Specifies the id of the window in which to embed the application, instead of it being created as an independent toplevel window. id must be specified in the same way as the value for the -use option for toplevel widgets (that is, it has a form like that returned by winfo_id()).
# NOTE: that on some platforms this will only work correctly if id refers to a Tk frame or toplevel that has its -container option enabled.
###

myroot.mainloop() # kick off the mainloop of the Tk class stored in myroot