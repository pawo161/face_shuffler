import requests
import shutil
import time
import numpy as np
import os.path
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True
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
    if (cc[2:][:-5]) == "-motion_detected":
        count += 1
        r = requests.get('https://thispersondoesnotexist.com/image',
                         stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open("img%s.jpeg" % (count), 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                start_time = time.time()
                #czasomierz
                print("start time: ", start_time)
                time.sleep(2)

                # wszystko w obecnym folderze z rozszerzeniem jpeg
                for f in os.listdir('.'):
                    if f.endswith('jpeg'):
                        rgbImg = Image.open(f)
                        rgbImg.load()
                        fn, fext = os.path.splitext(f)
                        # działanie

                        pix = np.array(rgbImg)
                        # doc on shuffle: multi-dimensional arrays are only shuffled along the first axis
                        # so let's make the image an array of (N,3) instead of (m,n,3)
                        rndImg2 = np.reshape(pix, (-1, pix.shape[2]))
                        b = random.randint(1, 6)
                        for k in range(b):
                            # now shuffle
                            np.random.shuffle(rndImg2)

                            # and reshape to original shape
                            rdmImg = np.reshape(rndImg2, pix.shape)
                            j = Image.fromarray(rdmImg, mode='RGB')

                            j.save('shuffled/%sS.jpeg' % (fn))
                            rndImg2 = rdmImg
                        #czasomierz
                        elapsed_time = time.time() - start_time
                        print("elapsed time: ", elapsed_time)
                        print(count)
                        break
#jak przyśpieszyć ten program? hash? fibonacci?
