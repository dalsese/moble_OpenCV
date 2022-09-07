import numpy as np
import cv2

cap = cv2.VideoCapture('./data/vtest.avi')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

imageFile = './data/lena.jpg'
img  = cv2.imread(imageFile) 
img_lisa = cv2.resize(img, (600, 600))

while True:   
    retval, frame = cap.read()

    if not retval:
        break
    img_frame = cv2.resize(frame, (600, 600)) # 안에서 꼭 사이즈 지정 해줘야함
    img_resize = cv2.addWeighted(img_frame,1,img_lisa,0.5,0)
    cv2.imshow('result', img_resize)
    
    key = cv2.waitKey(150)
    if key == 27: # Esc
        break
    
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
    
 ## 사진 합성과 편집
    
# path = './data/'
# imgAPP = cv2.imread(path+'apple.jpg')

# imageFile = './data/lena.jpg'
# img  = cv2.imread(imageFile) 

# cv2.imshow('Lena color',img) # 그냥

# resize_img = cv2.resize(img, (300, 300)) # 리사이즈
# cv2.imshow("resize img", resize_img)

# dst = cv2.bitwise_or(imgAPP, img) #src1_bg와 src2_fg를 합성
# cv2.imshow('Sum',dst)

# dst1 = cv2.addWeighted(img,0.5,imgAPP,1,0)
# cv2.imshow('Skin',dst1)
# cv2.destroyAllWindows()

