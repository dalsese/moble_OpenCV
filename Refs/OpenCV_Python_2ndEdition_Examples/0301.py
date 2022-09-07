#0301.py
import cv2
import numpy as np

# img = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255
#img = np.ones((512,512,3), np.uint8) * 255
#img = np.full((512,512,3), (255, 255, 255), dtype= np.uint8)
#img = np.zeros((512,512, 3), np.uint8) # Black 배경

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)

pt1 = 100, 100
pt2 = 400, 400

cv2.rectangle(img, pt1, pt2, (0, 255, 0), 20)
cv2.line(img, (100, 400), (400, 100), (255, 0, 0), 5)
cv2.line(img, pt1, pt2, (0,0,255), 5)

cv2.imwrite('./data/Lena.bmp', img)
imgBMP = cv2.imread('./data/Lena.bmp')
cv2.imshow('bmp.img', imgBMP)

img = np.zeros(shape=(512,512,3), dtype=np.uint8)
imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
cv2.rectangle(img, pt1, pt2, (0, 0, 0), 30)
cv2.line(img, (100, 400), (400, 100), (0, 0, 255), 30)
cv2.line(img, pt1, pt2, (255,0,0), 5)

cv2.imwrite('./data/Lena.png', img)
imgBMP1 = cv2.imread('./data/Lena.bmp')

cv2.imshow('png.img', imgBMP1)

cv2.waitKey()
cv2.destroyAllWindows()
