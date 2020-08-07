from cv2 import cv2
img=cv2.imread('dhoni.jpg')
cv2.imshow('original',img)
cv2.namedWindow('Adjust')
def nothing(x):
    pass
cv2.createTrackbar('lower threshold','Adjust',0,500,nothing)
cv2.createTrackbar('higher threshold','Adjust',0,500,nothing)

while(1):
    lt=cv2.getTrackbarPos('lower threshold','Adjust')
    ht=cv2.getTrackbarPos('higher threshold','Adjust')
    cannyimg=cv2.Canny(img,lt,ht)
    cv2.imshow('Output',cannyimg)
    cv2.imwrite('canny_thres.png',cannyimg)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break




