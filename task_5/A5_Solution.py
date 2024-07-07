import cv2
import numpy as np

cam = cv2.VideoCapture('./task_5/green_screen.mp4')
background = cv2.imread('./task_5/bg.jpg')  
window_width = 800    
window_height = 500  
 
cv2.namedWindow('Virtual Background', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Virtual Background', window_width, window_height)
while True:
    ret, frame = cam.read()
    if not ret:
        break
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerBound = np.array([40, 40, 40])
    upperBound = np.array([80, 255, 255])
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)
    mask_inv = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    background_part = cv2.bitwise_and(background, background, mask=mask)
    result = cv2.add(foreground, background_part)
    
    
    cv2.imshow('Virtual Background', result)
    cv2.resize(result,(250,250))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()