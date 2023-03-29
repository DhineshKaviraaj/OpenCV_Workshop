import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img[:]=255,0,0
cv2.line(img,(0,0),(img.shape[0],img.shape[1]),(0,255,255),3)
cv2.rectangle(img,(0,0),(400,100),(0,255,255),cv2.FILLED)
cv2.circle(img,(250,250),(100),(255,255,0),4)
cv2.putText(img,"OpenCV",(100,300),cv2.FONT_HERSHEY_SIMPLEX,3,(0,150,150),2)
cv2.imshow("Image",img)
cv2.waitKey()
