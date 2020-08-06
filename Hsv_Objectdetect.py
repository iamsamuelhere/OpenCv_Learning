from cv2 import cv2
import numpy as np
def nothing(x):
    pass
cam=cv2.VideoCapture(0)
cv2.namedWindow('Window')
cv2.createTrackbar('lh','Window',0,255,nothing)
cv2.createTrackbar('ls','Window',0,255,nothing)
cv2.createTrackbar('lv','Window',0,255,nothing)
cv2.createTrackbar('uh','Window',255,255,nothing)
cv2.createTrackbar('us','Window',255,255,nothing)
cv2.createTrackbar('uv','Window',255,255,nothing)
while(1):
    ret,img=cam.read()

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos('lh','Window')
    l_s=cv2.getTrackbarPos('ls','Window')
    l_v=cv2.getTrackbarPos('lv','Window')

    u_h=cv2.getTrackbarPos('uh','Window')
    u_s=cv2.getTrackbarPos('us','Window')
    u_v=cv2.getTrackbarPos('uv','Window')

    lb=np.array([l_h,l_s,l_v])
    ub=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv_img,lb,ub)
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)
    cv2.imshow('img',img)

    k=cv2.waitKey(1)
    if(k==27):
        break
cam.release()