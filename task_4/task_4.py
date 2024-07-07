 # importing required libraries
import cv2
import numpy as np

 # Global variables shared between the mouseClick function and rest of the code
draw = False
p1 = (0,0) # top left cornor point
p2 = p1 # bottom right cornor point

 # Mouse callback function
def mouseClick(event,xPos,yPos,flags,param):
    global draw,p1,p2 
    if event==cv2.EVENT_LBUTTONDOWN:
        draw = True
        p1 = (xPos,yPos)
        p2 = p1
    if event==cv2.EVENT_MOUSEMOVE and draw:
 	    p2 = (xPos,yPos)
    if event==cv2.EVENT_LBUTTONUP:
        draw = False

frame = np.zeros((500,500,3), np.uint8)

 # Creating an window to display image/frame
cv2.namedWindow('FRAME')  

 # This function detects every new events and triggers the "mouseClick" function
cv2.setMouseCallback('FRAME',mouseClick)

while True:
     frame = np.zeros((500,500,3), np.uint8) # renew black frame in every loop (this simulates a video)
     cv2.rectangle(frame,p1,p2,(0,255,0),2)
     cv2.imshow('FRAME',frame)
     if cv2.waitKey(1) & 0xff == ord('q'): # to quit press 'q'
 	    break
cv2.destroyAllWindows()