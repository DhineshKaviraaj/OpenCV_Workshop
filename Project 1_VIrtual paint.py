import cv2
import numpy as np

cap = cv2.VideoCapture(0)               # 0 for webcam
cap.set(3,640)                          # id 3 is width and 4 is height
cap.set(4,480)

myColors = [[5,107,0,19,255,255],[133,56,0,159,156,255],[57,76,0,100,255,255]]
# hmin hmax smin smax vmin vmax values for orange, purple, green
myColorValues = [[51,153,255],[255,0,255],[0,255,0]]
def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count=0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y= getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        count+=1
        # cv2.imshow("Color",mask)

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
                # cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
                peri = cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt,0.02*peri,True)
                x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cv2.destroyAllWindows()
# test
