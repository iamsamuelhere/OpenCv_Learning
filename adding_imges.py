from cv2 import cv2
img1=cv2.imread('dhoni.jpg')
img2=cv2.imread('opencvlogo.png')

img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

out=cv2.add(img1,img2)
weightout=cv2.addWeighted(img1,0.5,img2,0.5,0.3)


cv2.imshow('outputAdd',out)
cv2.imshow('outputaddweight',weightout)
cv2.waitKey()