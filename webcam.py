import cv2
cap = cv2.VideoCapture(0)               # 0 for webcam
cap.set(3,640)                          # id 3 is width and 4 is height
cap.set(4,480)

while True:
    success, img= cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
