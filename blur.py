from cv2 import cv2
img=cv2.imread('lady.jfif')
built_blurimg=cv2.blur(img,(5,5))
gausian_img=cv2.GaussianBlur(img,(5,5),0)
median_img=cv2.medianBlur(img,5)
bilateral_img=cv2.bilateralFilter(img,9,75,75)

cv2.imshow('ori',img)
cv2.imshow('blur()',built_blurimg)
cv2.imshow('gauss()',gausian_img)
cv2.imshow('median_img()',median_img)
cv2.imshow('bilateralimg()',bilateral_img)
cv2.waitKey()

