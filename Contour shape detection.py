import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 40:              # we use this to avoid detecting noise (noise can have less contour are)
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)                        # finding length of contour
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)         # gives a contour that is an approximate shape of the given contour
            print(len(approx))                                    # no. of points in detected shape's contour
            objCor = len(approx)                                  #no. of corners in objects
            x,y,w,h = cv2.boundingRect(approx)                    # returns the start coordinates (x,y) of detected object and also the width and height of bounding box required ; end coordinates = (x+w,y+h)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,0),2)


img = cv2.imread(r"C:\Users\kdhin\Desktop\opencv\c.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
cv2.imshow("Image",img)
cv2.imshow("ImageCanny",imgCanny)
cv2.imshow("ImageContour",imgContour)

cv2.waitKey(0)
