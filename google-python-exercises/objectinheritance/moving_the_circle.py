
from Tkinter import *
import time
class applaction:
    
    def __init__(self,master):
       
       self.master =master
       self.fun()
       self.c = Canvas(width=300, height=300, bg='white')
       self.c.pack(expand=YES, fill=BOTH) 
       self.fun2()
    def fun(self):
        self.lab=Label(self.master,text = " moving the circle")
        self.lab.pack()

        self.but= Button(self.master, text=" click me ", command = self.moving)
        self.but.pack()
        
    def moving(self): 
        numy=20
        for i in range(10):
            self.c.delete(self.z)
            time.sleep(.05)
            self.z=self.c.create_oval(100 ,100+numy,30,30+numy,width=2,fill='red')
            numy += 20
            self.c.update()
            
    def fun2(self):
        self.z=self.c.create_oval(100 ,100,30,30,width=2,fill='red')
        
root = Tk()

a = applaction(root)
root.mainloop()
