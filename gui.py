from tkinter import *
#import tkinter 
import time
from subprocess import Popen

Freq = 2500
Dur = 150

top = Tk()
top.title('AUTOEMAIL SENDER')
top.geometry('600x300')

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "E:\python\\Email_30017.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
def start():
    import os
    print ("Start")
#    os.system("python test.py")
    Popen(["python", "autoemail.py"])


def stop():
    print ("Stop")
    top.destroy()

startButton =Button(top, height=2, width=20, text ="Start", command = start)
stopButton = Button(top, height=2, width=20, text ="Stop", command = stop)
'''
startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
stopButton.place(relx=0.5, rely=0.5, anchor=CENTER)
'''
startButton.pack()
stopButton.pack()
top.mainloop()