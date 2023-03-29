import cv2
import numpy as np

img = cv2.imread(r"C:\Users\kdhin\Downloads\opencv\b.png")
print(img.shape)
#resize
imgResize = cv2.resize(img,(800,200))
#cropping using matrix functionality
imgCropped = img[0:300,0:500]            # note: first parameter is height (0:300) and next i s width (0:500)

cv2.imshow("Image",imgCropped)
cv2.waitKey()