# The cv2.waitKey() function:
# waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
# It takes time in milliseconds as a parameter and waits for the given time to destroy the window, if 0 is passed in the
# argument it waits till any key is pressed.
# if 0 is given as parameter instead of a time period the window is closed when any input is given.

import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kdhin\Downloads\The_Orion_Building-scaled.jpg")
kernel = np.ones((5,5),np.uint8)

#grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gaussian blur
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#canny edge detector
imgCanny = cv2.Canny(img,100,100)
#dilation
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
#erosion
eroded = cv2.erode(imgDilation,kernel,iterations=2)

imgCanny1 = cv2.resize(imgCanny,(1250,700))
imgDilate1 = cv2.resize(imgDilation,(1250,700))
imgEroded1 = cv2.resize(eroded,(1250,700))

cv2.imshow("Image0",imgCanny1)
#cv2.imshow("Image1",imgDilate1)
#cv2.imshow("Image2",imgEroded1)




cv2.waitKey()