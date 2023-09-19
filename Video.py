import cv2
import os
import OCR

#vidcap = cv2.VideoCapture('yt.mp4')
    
def getFrame(path, sec):
    count = 1
    vidcap = cv2.VideoCapture(path)
    print(path)
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    fr = 0.5
    print(hasFrames)
    while hasFrames :
        OCR.extract(image)
        count+=1  
        #print(count)
        sec+=fr
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
    print('done')

OCR.rm()

''' 

sec = 0
 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)'''