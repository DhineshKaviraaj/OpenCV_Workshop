# code from gfg

import cv2
import numpy as np

# Turn on Laptop's webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    # Locate points of the documents
    # or object which you want to transform
    pts1 = np.float32([[0, 260], [640, 260],
                       [0, 400], [640, 400]])
    pts2 = np.float32([[0, 0], [400, 0],
                       [0, 640], [400, 640]])

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))

    # Wrap the transformed image
    cv2.imshow('frame', frame)  # Initial Capture
    cv2.imshow('frame1', result)  # Transformed Capture

    if cv2.waitKey(24) == 27:
        break

cap.release()
cv2.destroyAllWindows()







"""
import cv2
import numpy as np

img= cv2.imread(r"C:\Users\kdhin\Downloads\cards on a table.jpg")
width,height = 250,350

pts1= np.float32([[357,289],[502,132],[491,277],[334,148]])       # storing coordinates as list of lists of type float32
pts2= np.float32([[0,0],[width,0],[width,height],[0,height]])     # Note that the np.float32() function is used to convert the list of lists to a NumPy array of 32-bit floating point numbers for numerical computations.
matrix= cv2.getPerspectiveTransform(pts1,pts2)
warpedimg= cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warped image",warpedimg)
cv2.waitKey(0)

"""




#(357,289),(491,277),(502,132),(334,148)

"""
cv2.getPerspectiveTransform method

Syntax: cv2.getPerspectiveTransform(src, dst)

Parameters:

src: Coordinates of quadrangle vertices in the source image.
dst: Coordinates of the corresponding quadrangle vertices in the destination image.
cv2.wrapPerspective method

Syntax: cv2.warpPerspective(src, dst, dsize)

Parameters:

src: Source Image
dst: output image that has the size dsize and the same type as src.
dsize: size of output image
"""
