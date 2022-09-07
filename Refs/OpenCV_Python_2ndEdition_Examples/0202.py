# 0202.py
import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) #정보를 읽어서 저장한다.

cv2.imwrite('./data/Lena.bmp', img)
imgBMP = cv2.imread('./data/Lena.bmp')
cv2.imshow('bmp.img', imgBMP)

cv2.imwrite('./data/Lena.png', img)
imgBMP1 = cv2.imread('./data/Lena.bmp')
cv2.imshow('png.img', imgBMP1)

cv2.imwrite('./data/Lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100])

imageFile = './data/lena2.jpg'
img = cv2.imread(imageFile) #정보를 읽어서 저장한다.
cv2.imshow('Lena quality',img)
cv2.waitKey()
cv2.destroyAllWindows()
