#coding:utf-8


import time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
	#お決まり
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
	
#		self.label1 = tk.Label(self, text='Hello everybody.',  bg='yellow', relief=Tk.RIDGE, bd=2)


#		self.label1 = tk.Label(text='Hello everybody.')
#		self.label1.pack()
#		self.label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)   

#   	self.l1=tk.Label(text='text')
#        self.l1.pack()


        self.label1=tk.Label(text='aaaaa')
#        self.label1.pack()
        self.label1.grid(row=0, column=0)  
        self.label1.pack()
#        self.label2=tk.Label(text='bbbbb')
#        self.label2.grid(row=1, column=0)  
        

        
	#１つめのbutton        
#        self.hi_there = tk.Button(self)
#        self.hi_there["text"] = "Hello World\n(click me)"
#        self.hi_there["command"] = self.say_hi
#        self.hi_there.pack()

#        self.hi_there.pack(side="top") #配置

#        self.l1=tk.Label(text='text')
#        self.l1.pack()

	#２つめのbutton
#        self.QUIT = tk.Button(self, text="QUIT", fg="red",
#                                            command=root.destroy)
#        self.QUIT.pack()
#        self.QUIT.pack(side="bottom")#配置

#    def say_hi(self):
#        print("hi there, everyone!")



root = tk.Tk()
app = Application(master=root)
app.mainloop()



#tk=tkinter.Tk()
#tk = Application(master=root)
#tk.mainloop()



