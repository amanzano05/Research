import cv2
import numpy as np

cenX=0
cenY=0
centered=False
faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#windows-> (cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
videoCapture=cv2.VideoCapture(0)
if not (videoCapture.isOpened()):
    print("Could not open video device")
else:
    videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
    videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    while 1:
        ret, pic =videoCapture.read()
        pic=cv2.flip(pic,1)
        height, width, channels= pic.shape
        centerImageX=int(width/2)
        centerImageY=int (height/2)
        correctPositionXstart=centerImageX-20
        correctPositionXend=centerImageX+20
        correctPositionYstart=centerImageY-20
        correctPositionYend=centerImageY+20
        print("h: "+str(centerImageX)+ " w: " + str(centerImageY))
        grayFrame=cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(grayFrame,
                                           scaleFactor=1.07,
                                           minNeighbors=5,
                                           minSize=(30,30),
                                           flags = cv2.CASCADE_SCALE_IMAGE)

        for (x,y,w,h) in faces:
            cenX = int(x + (w/2))
            cenY = int((y + (h/2)))
            if not centered:
                cv2.rectangle(pic,(x,y), (x+w, y+h),(255,0,0),2)
            else:
                cv2.rectangle(pic, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(pic, (cenX-5, cenY-5) , (cenX + 5, cenY + 5), (0, 255, 0), 2)
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(pic, 'Me',(x,y),font,2,(255,255,255),2,cv2.LINE_AA)
       # print("Number of faces found {} ".format(len(faces)))
        print("position x: {x}, position y:{y}".format(x=cenX, y=cenY))
        if ((cenX>=correctPositionXstart and cenX<=correctPositionXend) and (cenY>=correctPositionYstart and cenY<=correctPositionYend)):
            centered=True
            print("Correct position")
        elif (cenX<correctPositionXstart):
            print("Move right")
            centered=False
        elif(cenX>correctPositionXend):
            print("Move left")
            centered = False
        elif(cenY<correctPositionYstart):
            print("Move down")
            centered = False
        elif(cenY>correctPositionYend):
            print("Move up")
            centered = False
        cv2.rectangle(pic, (correctPositionXstart, correctPositionYstart), (correctPositionXend, correctPositionYend), (0, 0, 0), 2)
        cv2.imshow('face', pic)
        k=cv2.waitKey(30) & 0xff
        if k==27:
            break
videoCapture.release()
cv2.destroyAllWindows()