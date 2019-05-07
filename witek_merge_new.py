import requests
import shutil
#import time
import numpy as np
import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import random
#import keyboard
import serial
count = 0
#serial communication with arduino
ser1 = serial.Serial('/dev/cu.usbmodem14201', 9600)
ser1.readline()
while True:
    cc = str(ser1.readline())
    print(cc[2:][:-5] )
    if (cc[2:][:-5]) == "motion_detected":
        count += 1
        r = requests.get('https://thispersondoesnotexist.com/image',
                         stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open("img%s.jpeg" % (count), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

                #czasomierz
                #start_time = time.time()
                #print("start time: ", start_time)
                #time.sleep(1)

                # wszystko w obecnym folderze z rozszerzeniem jpeg

                rgbImg = Image.open("img%s.jpeg" % (count))
                #rgbImg.load()
                #rgbImg.LOAD_TRUNCATED_IMAGES = True
                #fn, fext = os.path.splitext(f)
                # działanie

                pix = np.array(rgbImg)
                 # doc on shuffle: multi-dimensional arrays are only shuffled along the first axis
                # so let's make the image an array of (N,3) instead of (m,n,3)
                rndImg2 = np.reshape(pix, (-1, pix.shape[2]))
                b = random.randint(1, 5)
                for k in range(b):
                    # now shuffle
                    np.random.shuffle(rndImg2)

                    # and reshape to original shape
                    rdmImg = np.reshape(rndImg2, pix.shape)
                    j = Image.fromarray(rdmImg, mode='RGB')

                    j.save('shuffled/img%sS.jpeg' % (count))
                    rndImg2 = rdmImg

                #czasomierz
                #elapsed_time = time.time() - start_time
                #print("elapsed time: ", elapsed_time)
                print(count)
                if count > 2:
                    os.remove("shuffled/img%sS.jpeg" % (count-2))
                    os.remove("img%s.jpeg" % (count-2))

#jak przyśpieszyć ten program? hash? fibonacci?
