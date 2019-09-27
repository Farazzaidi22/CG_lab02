from tkinter import *

root = Tk()

can = Canvas(root, width = 100, height = 400, bg= 'blue')

def printt(event):
    print(event.x, event.y)

can.bind("<Button-1>", printt)

can.pack()

root.mainloop()