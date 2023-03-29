# General theory :
# Link 1 : https://learnopencv.com/color-spaces-in-opencv-cpp-python/
# What is an HSV image ?
# HSV image: Hue - Saturation - Value image
# inRange() function :
# resultarray = inRange(sourcearray, upperboundarray, lowerboundarray)
# https://www.educba.com/opencv-inrange/
# Functions used :
# cv2.createTrackbar(trackbar_name, window_name, default_value, max_value, callback_func)
# cv2.getTrackbarPos(trackbar_name, window_name)
# bitwise_and(source1_array, source2_array, destination_array, mask)
# Parameters :
# trackbar_name − It's the trackbar name. This name is used to access the trackbar position value.
# window_name − It is the name of the window to which the trackbar is attached.
# default_value − default value set for the trackbar.
# max_value − maximum value for the trackbar.
# callback_func − function executed when trackbar value changes.


import cv2
import numpy as np
def empty(a):         # empty funcction created to be put as argument to createTrackbar() function    #
    pass

# convert rgb to hsv
img= cv2.imread(r"C:\Users\kdhin\Desktop\opencv\b.png")
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# creating a window called trackbars to hold our trackbars & resizing it
cv2.namedWindow("TrackBars")                                                     #
cv2.resizeWindow("TrackBars",640,240)                                            #
# creating trackbars for hue,sat and value min & max
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)                            #       # value of max_value of hue is more than 300 but opencv supports only upto 180 (0-179) values of HUE
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while(True):
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")                            #
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)                                        #
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Mask", mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)                                # cv2.waitKey(1) : 1 is used as parameter because we want the output to be printed for 1ms before the next iteration takes palce and the corresponding output is printed
                                                  # if 0 is given instead of 1; every loop iteration will happen only after key press
