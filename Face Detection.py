import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(r"C:\Users\kdhin\Desktop\opencv\haarcascade_frontalface_default.xml")
img = cv2.imread(r"C:\Users\kdhin\Desktop\opencv\faces.png")
img = cv2.resize(img,(800,400))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,1)          # detectMultiScale returns the bounding rectangle info in the order x,y,w,h
for x,y,w,h in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0))

cv2.imshow("Image",img)
cv2.waitKey(0)
