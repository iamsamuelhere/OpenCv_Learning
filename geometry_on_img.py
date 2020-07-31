from cv2 import cv2
#drawing line 
app=cv2.imread('apple.jfif')
out=cv2.arrowedLine(app,(0,0),(50,50),(255,0,0),5)
out=cv2.rectangle(app,(60,60),(100,100),(0,255,0),5)
out=cv2.circle(out,(150,150),30,(50,50,50),-1)
out=cv2.line(out,(90,90),(200,200),(10,10,10),4)
cv2.imshow('output',out)
cv2.waitKey()