import time
from tkinter import *

root = Tk()

photo_ball = PhotoImage(file ='C:\\Users\\Faraz_0hm6\\OneDrive\\Desktop\\basketball.png')

def pic():
    canvas = Canvas(root,width =200, height =200, bg= 'white')
    canvas.pack()
    canvas.create_image(0,0, image= photo_ball, anchor= NW)
    
Label(root, text = 'Press start to display image', font =('Verdana', 15)).pack(side = TOP, pady = 10)

frame = Frame(root)
button1 = Button(frame, text="Play", command = pic)
button1.pack(side = LEFT)

frame.pack()

root.mainloop()