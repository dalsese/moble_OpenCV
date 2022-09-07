# 0210.py
import cv2

#cap = cv2.VideoCapture(0) # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print('frame_size =', frame_size)

# fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter('./data/record0.mp4',fourcc, 20.0, frame_size)
out2 = cv2.VideoWriter('./data/record1.mp4',fourcc, 20.0, frame_size,isColor=False) # 흑백

while True: # 무한루프
    retval, frame = cap.read()
    if not retval:
        break   
    out1.write(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)        
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)      
    
    key = cv2.waitKey(0)
    
    if key == 27: # 27번 키는 ESC
        break
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
