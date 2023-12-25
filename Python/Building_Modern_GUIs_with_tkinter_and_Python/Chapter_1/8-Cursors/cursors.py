from tkinter import *

root = Tk()
root.geometry('606x1080')

# cursors: arrow, clock, cross, circle, heart, mouse, plus, star, spider, sizing, shuttle, target, tcross, trek, watch, etc.
arrow_button        =   Button(root,
                               text     = 'arrow',
                               relief   = 'raised',
                               cursor   = 'arrow',
                               width    = 13,
                               bd       = 2)

clock_button        =   Button(root,
                               text     = 'clock',
                               relief   = 'raised',
                               cursor   = 'clock',
                               width    = 13,
                               bd       = 2)

cross_button        =   Button(root,
                               text     = 'cross',
                               relief   = 'raised',
                               cursor   = 'cross',
                               width    = 13,
                               bd       = 2)

circle_button       =   Button(root,
                               text     = 'circle',
                               relief   = 'raised',
                               cursor   = 'circle',
                               width    = 13,
                               bd       = 2)

heart_button        =   Button(root,
                               text     = 'heart',
                               relief   = 'raised',
                               cursor   = 'heart',
                               width    = 13,
                               bd       = 2)

mouse_button        =   Button(root,
                               text     = 'mouse',
                               relief   = 'raised',
                               cursor   = 'mouse',
                               width    = 13,
                               bd       = 2)

plus_button         =   Button(root,
                               text     = 'plus',
                               relief   = 'raised',
                               cursor   = 'plus',
                               width    = 13,
                               bd       = 2)

star_button         =   Button(root,
                               text     = 'star',
                               relief   = 'raised',
                               cursor   = 'star',
                               width    = 13,
                               bd       = 2)

spider_button       =   Button(root,
                               text     = 'spider',
                               relief   = 'raised',
                               cursor   = 'spider',
                               width    = 13,
                               bd       = 2)

sizing_button       =   Button(root,
                               text     = 'sizing',
                               relief   = 'raised',
                               cursor   = 'sizing',
                               width    = 13,
                               bd       = 2)

shuttle_button      =   Button(root,
                               text     = 'shuttle',
                               relief   = 'raised',
                               cursor   = 'shuttle',
                               width    = 13,
                               bd       = 2)

target_button       =   Button(root,
                               text     = 'target',
                               relief   = 'raised',
                               cursor   = 'target',
                               width    = 13,
                               bd       = 2)

tcross_button       =   Button(root,
                               text     = 'tcross',
                               relief   = 'raised',
                               cursor   = 'tcross',
                               width    = 13,
                               bd       = 2)

trek_button         =   Button(root,
                               text     = 'trek',
                               relief   = 'raised',
                               cursor   = 'trek',
                               width    = 13,
                               bd       = 2)

watch_button        =   Button(root,
                               text     = 'watch',
                               relief   = 'raised',
                               cursor   = 'watch',
                               width    = 13,
                               bd       = 2)

arrow_button.pack()
clock_button.pack()
cross_button.pack()
circle_button.pack()
heart_button.pack()
mouse_button.pack()
plus_button.pack()
star_button.pack()
spider_button.pack()
sizing_button.pack()
shuttle_button.pack()
target_button.pack()
tcross_button.pack()
trek_button.pack()
watch_button.pack()

root.mainloop()