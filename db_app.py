#!/bin/python
import os
#from Tkinter import *
import Tkinter
import subprocess as sub

#p=sub.Popen('./script', stdout=sub.PIPE,stderr=sub.PIPE)
#output, errors = p.communicate()

class Application(Frame):

    def ask_pass(self):
        '''
        ask = Frame(app, height=100, width=200)
        p=sub.Popen(["~/script2.sh"], stdout=sub.PIPE, stderr=sub.PIPE)
        output = p.communicate()[0]
        text=Text(root)
        text.pack()
        text.insert(END, output)
        '''
        test=sub.Popen(["ping", "-W", "2", "-c", "1", "8.8.8.8"], stdout=sub.PIPE)
        output = test.communicate()[0]

    def print_db(self):
        global flag
        termf = Frame(app, height=200, width=400)
        termf.pack(fill=BOTH, expand=YES)
        wid=termf.winfo_id()
        if (flag == 0):
            os.system('xterm -into %d -geometry 100x100 -sb -e ~/script.sh &' % wid)
            flag = 1
        else:
            os.system('~/script.sh' % wid)

    def createW(self):
        self.q=Button(self)
        self.q["text"]="Quit"
        self.q["fg"]="red"
        self.q["command"]=self.quit
        self.q.pack({"side":"left"})

        self.db_print=Button(self)
        self.db_print["text"]="print DB"
        self.db_print["command"]=self.ask_pass
        self.db_print.pack({"side":"right"})

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createW()

flag = 0
root=Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
