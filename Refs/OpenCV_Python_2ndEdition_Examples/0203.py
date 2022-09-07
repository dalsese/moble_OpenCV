# 0203.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgBGR = cv2.imread(imageFile)
plt.imshow(imgBGR)
plt.axis('off')

imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB) ## cvtColor 사용, BGR을 RGB로 바꿔라 
plt.imshow(imgRGB)
plt.show()
