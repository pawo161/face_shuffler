import requests
import shutil
import time
import numpy as np
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
#import random
#import keyboard
#pip install pyserial
import serial
from tkinter import *
import sys, os
import tkinter
import time
from PIL import Image, ImageTk
# from gif_module import AnimatedGIF
# import gif_module
count = 0
def wyswietlanie():
    
    # root = Tk()     

    
    # w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    # root.overrideredirect(1)
    # root.focus_set()
    # root.geometry("%dx%d+1366+0" % (w, h))

    root2 = Toplevel()
    root2.focus_set()
    root2.overrideredirect(1)
    root2.title("My debug window")
    root2.geometry('%dx%d+%d+%d'%(1366,768,0,0)) 

   
    img = ImageTk.PhotoImage(Image.open('img%d.jpeg' % count))
    panel = Label(root2, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    # l = gif_module.AnimatedGIF(root,'\\Users\Justyna\Desktop\zdj2\shuffled\img%dS.gif' % count)
    # l.pack()

    root2.update_idletasks()
    root2.update()
    

    # root.update_idletasks()
    # root.update_idletasks()
    
    
#serial communication with arduino
# ser1 = serial.Serial('/dev/cu.usbmodem14201', 9600)
# ser1.readline()
while True:
    # cc = str(ser1.readline())
    # print(cc[2:][:-5] )
    # m = input()
    # if (cc[2:][:-5]) == "motion_detected":
    for i in range(40):
        
        count += 1
        r = requests.get('https://thispersondoesnotexist.com/image',
                         stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open("img%s.jpeg" % (count), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                print("saved raw")

                #czasomierz
                start_time = time.time()
                print("start time: ", start_time)


                rgbImg = Image.open("img%d.jpeg" % (count))
                #rgbImg.load()
                #rgbImg.LOAD_TRUNCATED_IMAGES = True
                #fn, fext = os.path.splitext(f)
                # działanie

                pix = np.array(rgbImg)
                 # doc on shuffle: multi-dimensional arrays are only shuffled along the first axis
                # so let's make the image an array of (N,3) instead of (m,n,3)
                rndImg2 = np.reshape(pix, (-1, pix.shape[2]))
                #b = random.randint(5,9)
                images = []
                for k in range(4):
                    # now shuffle
                    np.random.shuffle(rndImg2)

                    # and reshape to original shape
                    rdmImg3 = np.reshape(rndImg2, pix.shape)

                    j = Image.fromarray(rdmImg3, mode='RGB')

                    images.append(j)

                j.save('img%dS.gif' % (count), format='GIF', append_images=images[0:], save_all=True, duration=37, loop=0)
                os.startfile('img%dS.gif' % (count), 'open')
                #rndImg2 = rdmImg
                print("saved gif")
                #czasomierz
                elapsed_time = time.time() - start_time
                print("elapsed time: ", elapsed_time)
                
                    
                
                wyswietlanie()
                
                
                
                
                print(count)
                # if count > 2:
                #     os.remove("\\Users\Justyna\Desktop\zdj2\shuffled\img%sS.gif" % (count-2))
                #     os.remove("\\Users\Justyna\Desktop\zdj2\img%s.jpeg" % (count-2))

#Chrome jako domyslny odtwarzacz gif. Chrome odpalony na zewnetrznym ekranie przyjmuje gify.





