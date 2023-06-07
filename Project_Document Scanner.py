import cv2
import numpy as np
# cap = cv2.VideoCapture(0)               # 0 for webcam
# cap.set(3,640)                          # id 3 is width and 4 is height    # to set brightness, id is 10
# cap.set(4,480)

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres = cv2.erode(imgDial,kernel,iterations=1)
    return imgThres


def getContours(img):
    biggest = np.array([])
    maxArea=0
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
                # cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
                peri = cv2.arcLength(cnt,True)
                approx = cv2.approxPolyDP(cnt,0.02*peri,True)
                if area>maxArea and len(approx)==4:
                    biggest = approx
                    maxArea=area
    cv2.drawContours(imgContour,biggest,-1,(255,0,0),20)
    return biggest


def getWarp(img,biggest):
    pass



while True:
    # success, img= cap.read()
    img = cv2.imread(r"C:\Users\kdhin\Desktop\opencv\opencv try.png")
    # cv2.resize(img,(640,480))
    img = cv2.resize(img,(640,480))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    print(biggest)
    getWarp(img,biggest)
    cv2.imshow("Video",imgContour)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
