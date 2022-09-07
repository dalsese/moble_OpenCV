#0310.py
import keyboard
import numpy as np
import cv2
import pyautogui 

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0 # right

while True:   
    key = cv2.waitKeyEx(30)    
    if key == 0x1B: 
        break;
# 방향키 방향전환 
    elif pyautogui.keyDown(key == 0x270000): # right
        direction = 0
    elif pyautogui.keyDown(key == 0x280000): # down
        direction = 1
    elif pyautogui.keyDown(key == 0x250000): # left
        direction = 2
    elif pyautogui.keyDown(key == 0x260000): # up
        direction = 3
    elif pyautogui.keyDown(key == 0x270000 & key == 0x260000): # right up
        direction = 4
    elif pyautogui.keyDown(key == 0x250000 & key == 0x260000): # left up
        direction = 5
    elif pyautogui.keyDown(key == 0x270000 & key == 0x280000): # right down
        direction = 6
    elif pyautogui.keyDown(key == 0x250000 & key == 0x280000): # left down
        direction = 7
        
# 방향으로 이동 
    if direction == 0:     # right
        x += 10
    elif direction == 1:   # down
        y += 10
    elif direction == 2:   # left
        x -= 10
    elif direction == 3:   
        y -= 10
    elif direction == 4:  
        x += 10
        y -= 10
    elif direction == 5:  
        x -= 10
        y -= 10
    elif direction == 6:  
        x += 10
        y += 10
    elif direction == 7:  
        x -= 10
        y += 10
        
#   경계확인 
    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3
        
# 지우고, 그리기        
    img = np.zeros((width, height,3), np.uint8) + 255 # 지우기
    cv2.circle(img, (x, y), R, (0, 0, 255), -1) 
    cv2.imshow('img', img)
    
cv2.destroyAllWindows()
