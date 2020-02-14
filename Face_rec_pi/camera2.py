import picamera.array #used to import the frame as array
import picamera #for accesing the camera
import time #used to pause the program for warming the camera
import cv2 #used to proces the picture
import numpy as np

myCam = picamera.PiCamera() 

myCam.resolution=(1024, 768)
myCam.framerate=32
rawCapture = picamera.array.PiRGBArray(myCam, size=(1024, 768))

time.sleep(0.1)

for eachFrame in myCam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = eachFrame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break
cv2.destroyAllWindows()






