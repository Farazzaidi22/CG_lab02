from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
root = Tk()


def openThisPc():
    path=filedialog.askopenfilename(filetypes=[("Image File",'.png')])
    im = Image.open(path)
    tkimage = ImageTk.PhotoImage(im)
    myvar=Label(root,image = tkimage)
    myvar.image = tkimage
    myvar.pack()

Label(root, text = 'Press Select image to choose an image from your pc', font =('Verdana', 15)).pack(side = TOP, pady = 10)
frame = Frame(root)
button1 = Button(frame, text="Select image", command = openThisPc)
button1.pack(side = LEFT)

frame.pack()
 
root.mainloop()