# 0410.py
import cv2
import numpy as np
 
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE) # 흑백
print("shape",src.shape) # shape(512, 512)
shape = src.shape[0], src.shape[1], 3 # shape(512, 512, 3) 즉, 칼라
dst = np.zeros(shape, dtype=np.uint8)

dst[:,:,0] = src  # B
##dst[:,:,1] = src # G
##dst[:,:,2] = src # R

dst[100:400, 200:300, :] = [255, 255, 255] #영역 전부 색상을 255

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()    
cv2.destroyAllWindows()
