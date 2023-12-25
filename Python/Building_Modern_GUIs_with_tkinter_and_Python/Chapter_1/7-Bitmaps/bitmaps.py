from tkinter import *

root = Tk()

root.geometry('505x350')

# bitmaps: error, gray12, gray25, gray50, gray75, info, hourglass, warning, question, questhead
error_button  = Button(root,
                       text     = 'sunken_error',
                       relief   = 'sunken',
                       bitmap   = 'error',
                       bd       = 2)
gray12_button = Button(root,
                       text     = "gray12",
                       relief   = 'sunken',
                       bitmap   = 'gray12',
                       bd       = 2)

gray25_button = Button(root,
                       text     = 'gray25',
                       relief   = 'sunken',
                       bitmap   = 'gray25',
                       bd       = 2)

gray50_button = Button(root,
                       text     = 'gray50',
                       relief   = 'sunken',
                       bitmap   = 'gray50',
                       bd       =2)

gray75_button = Button(root,
                       text     = 'gray75',
                       relief   = 'sunken',
                       bitmap   = 'gray75',
                       bd       =2)

info_button   = Button(root,
                       text     = 'info',
                       relief   = 'sunken',
                       bitmap   = 'info',
                       bd       = 2)

hour_button   = Button(root,
                       text     = 'hourglass',
                       relief   = 'sunken',
                       bitmap   = 'hourglass',
                       bd       = 2)

warn_button   = Button(root,
                       text     = 'warning',
                       relief   = 'sunken',
                       bitmap   = 'warning',
                       bd       = 2)

question_button=Button(root,
                       text     = 'question',
                       relief   = 'sunken',
                       bitmap   = 'question',
                       bd       = 2)

questhead_button=Button(root,
                        text    = 'questhead',
                        relief  = 'sunken',
                        bitmap  = 'questhead',
                        bd      = 2)

error_button.pack()
gray12_button.pack()
gray25_button.pack()
gray50_button.pack()
gray75_button.pack()
info_button.pack()
hour_button.pack()
warn_button.pack()
question_button.pack()
questhead_button.pack()

root.mainloop()