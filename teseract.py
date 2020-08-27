import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from cv2 import cv2
i=cv2.imread('handwri.jfif')
text=pytesseract.image_to_string(i)
print(text)
print("Number of words {} ".format(len(text.split())))
cv2.imshow('Output image',i)
cv2.waitKey()