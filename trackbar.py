from cv2 import cv2
import numpy as np
img=np.zeros((500,500,3),np.uint8)
cv2.namedWindow('window')
def nothing(x):
    pass
cv2.createTrackbar('b','window',0,255,nothing)
cv2.createTrackbar('g','window',0,255,nothing)
cv2.createTrackbar('r','window',0,255,nothing)
while(1):
    cv2.imshow('window',img)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
    b=cv2.getTrackbarPos('b','window')
    g=cv2.getTrackbarPos('g','window')
    r=cv2.getTrackbarPos('r','window')
    img[:]=[b,g,r]
