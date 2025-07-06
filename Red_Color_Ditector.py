## To run it you need opencv and numpy do (pip install numpy opencv-python) in terminal
import cv2 as cv
import numpy as np

#If camara doesnt work change 0 with 1
web = cv.VideoCapture(0)
while True:
    isTrue, img = web.read()
    if isTrue:
        hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        Red_L = np.array([135,85,115],np.uint8)
        Red_U = np.array([185,250,250],np.uint8)
        Red_M = cv.inRange(hsv,Red_L,Red_U)
        kernal = np.ones((5,5),np.uint8)
        Red_M = cv.dilate(Red_M,kernal)
        red = cv.bitwise_and(img,img,mask = Red_M)
        cont, hier = cv.findContours(Red_M,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
        for pic, cont in enumerate(cont):
            area = cv.contourArea(cont)
            if (area>500):
                x,y,w,h = cv.boundingRect(cont)
                img = cv.rectangle(img,(x,y),(x+w,y+h),(0,0,225),2)
                cv.putText(img,"RED Color",(x,y),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255))
        cv.imshow("Red_coloe_Detector",img)


        if cv.waitKey(20) & 0xff == ord('q'):
            break
    else:
        break
web.release()
cv.destroyAllWindows()
