from Tkinter import *

from time import sleep
class applaction:
    
    def __init__(self,root):
       
       self.root =root
       self.lab=Label(self.root,text = " moving the circle")
       self.lab.pack()
       self.but= Button(self.root, text=" click me ")
       self.but.bind("<Button-1>",self.__moveCircle)
       
       self.but.pack()
        
      
       self.c = Canvas(root,width=300, height=300, bg='white')
       self.c.pack(expand=YES, fill=BOTH) 

       self.cir=self.c.create_oval(10 ,10,50,50,fill='red')
       
       #self.__drawCircle()


    def __moveCircle(self,event):
        self.__drawCircle()
        while self.c.coords(self.cir)[3] + 30 <self.c.winfo_reqheight():
            self.c.move(self.cir,0,3)
            sleep(0.01)
            self.root.update()

    
    def __drawCircle(self):
        #creat_oval return an intger which has the id
        self.c.delete(self.cir)
        self.cir=self.c.create_oval(10 ,10,50,50,fill='red')
        self.root.update()
        
root = Tk()

a = applaction(root)
root.mainloop()
