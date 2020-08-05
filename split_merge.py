from cv2 import cv2
img=cv2.imread('dhoni.jpg')

b,g,r=cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
m=cv2.merge((b,g,r))
cv2.imshow('merged',m)
cv2.waitKey()