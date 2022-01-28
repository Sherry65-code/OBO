import mod
from tkinter import *
# For testing

mod.clear_slate()

def listentovoice():
    query = mod.hear(0)
    mod.speak(mod.give_ans(query))
root = Tk()
root.geometry('220x220')
root.minsize(height=220,width=220)
root.maxsize(height=220,width=220)
root.iconbitmap('icon.ico')
root.title("OBO")
image1 = PhotoImage(file=r"mic.png")
Button(image=image1, height=200,width=200,command=listentovoice, relief=FLAT, borderwidth=0).pack()
root.mainloop()