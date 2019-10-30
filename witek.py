# from tkinter import *
import sys, os
import tkinter
import time
from PIL import Image, ImageTk

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='black')


def showPIL(pilImage):
    imgWidth, imgHeight = pilImage.size
 # resize photo to full screen 
    ratio = min(w/imgWidth, h/imgHeight)
    imgWidth = int(imgWidth*ratio)
    imgHeight = int(imgHeight*ratio)
    pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)   
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.update_idletasks()
    root.update()
   
#    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))


file=Image.open("\\Users\Justyna\Desktop\zdj1.jpg", mode="r")
file2=Image.open("\\Users\Justyna\Desktop\zdj3.jpg", mode="r")

while True:
    showPIL(file)
    # showPIL(file2)

# fd = os.open("/Users/pawelk/Downloads/output.jpg", os.O_RDWR)
# window = Tk()
# width_value=window.winfo_screenwidth()
# height_value=window.winfo_screenheight()
# canvas = tkinter.Canvas("%dx%d+0+0" % (width_value, height_value))
# canvas.pack()
# canvas.configure(background='black')


# window.geometry("%dx%d+0+0" % (width_value, height_value))
# window.mainloop()
