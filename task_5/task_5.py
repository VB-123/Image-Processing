# import required libraries
import cv2
import numpy as np

# Input video file
cam = cv2.VideoCapture('./task_5/ball.wmv')

while True:
    _, frame = cam.read()
    # converting to HSV for masking
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # lower and upper bound for color from last program
    lowerBound = np.array([110,80,134])#lower and upper boundary for color range in HSV
    upperBound = np.array([150,255,255])
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)#Creating Mask using the color range

    # Finding contours on masked frame
    ballContours,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) # contours around mask
    # If multiple set of sontours available, iterate through each
    for ballContour in ballContours:
        area = cv2.contourArea(ballContour)
        if area > 500: # to filter out noise. This avoids very small contours that could be noise
            x,y,w,h = cv2.boundingRect(ballContour) # this function returns position and size of bounding box for tracking
        # print(x,y,w,h)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) # draw rectangle arounf blue box

        cv2.imshow('mask', mask)
        cv2.imshow('Ball', frame)

    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
cam.release()
cv2.destroyAllWindows()