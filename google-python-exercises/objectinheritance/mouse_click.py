from Tkinter import *




root = Tk()

def rightClick(event):
    print 'right clicked'
    print event.x
    print event.y
   

def leftClick(event):
    print 'left clicked'
    print event.x
    print event.y
def middelClick(event):
    print 'middel clicked'

frame = Frame(root,width = 300, height = 300)
frame.bind("<Button-1>",leftClick)
frame.bind("<Button-2>",middelClick)
frame.bind("<Button-3>",rightClick)



frame.pack()
root.mainloop()
