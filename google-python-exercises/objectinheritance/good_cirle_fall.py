from Tkinter import *
import math
from time import sleep
class applaction:
    
    def __init__(self,root):
       
       self.root =root
       self.lab=Label(self.root,text = " moving the circle")
       self.lab.pack()

       
      
        
      
       self.c = Canvas(root,width=300, height=300, bg='white')
       self.c.pack(expand=YES, fill=BOTH) 
        
       self.c.bind("<Button-1>",self.__leftClick)
       #self.cir=self.c.create_oval(10 ,10,50,50,fill='red')
       
       #self.__drawCircle()
    """

    def __moveCircle(self,event):

        self.__drawCircle()
        while self.c.coords(self.cir)[3] + 30 <self.c.winfo_reqheight():
            self.c.move(self.cir,0,3)
            sleep(0.01)
            self.root.update()
    """
    
    def __drawCircle(self,event):
        #creat_oval return an intger which has the id
        #self.c.delete(self.cir)
        
   
        
        self.cir=self.c.create_oval( event.x ,event.y,event.x+40,event.y+40, fill='red')
        self.root.update()
    def __leftClick(self,event):
        self.__drawCircle(event)
        while self.c.coords(self.cir)[3] + 30 <self.c.winfo_reqheight():
            self.c.move(self.cir,0,3)
            sleep(0.01)
            self.root.update()


        
        print event.x
        print event.y
        
root = Tk()

a = applaction(root)
root.mainloop()
