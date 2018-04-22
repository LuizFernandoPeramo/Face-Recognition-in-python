import cv2
import numpy as np
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
ret,img=cap.read()
cv2.imshow('windowname',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
