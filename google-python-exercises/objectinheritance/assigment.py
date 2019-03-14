from Tkinter import *
import math
from time import sleep
class applaction:
    
    def __init__(self,root):
       
       self.root =root
       self.lab=Label(self.root,text = "The circle falling ")
       self.lab.pack()

       
      
        
      
       self.c = Canvas(root,width=500, height=500, bg='white')
       self.c.pack(expand=YES, fill=BOTH)

       self.g=self.c.create_rectangle(0, 400, 500, 500,fill="blue")

       
       self.c.bind("<Button-1>",self.__leftClick)

    
    def __drawCircle(self,event):        
        self.cir=self.c.create_oval( event.x ,event.y,event.x+40,event.y+40, fill='red')
        self.root.update()
        self.c.tag_lower(self.cir,self.g )
    def __leftClick(self,event):
        self.__drawCircle(event)
        while self.c.coords(self.cir)[3] + 30 <self.c.winfo_reqheight():
            self.c.move(self.cir,0,3)
            sleep(0.01)
            self.root.update()


        

        
root = Tk()

a = applaction(root)
root.mainloop()
