import cv2
import numpy as np

draw = False
p1 = (0,0)  # top left corner point
p2 = p1     # bottom right corner point

def mouseClick(event, xPos, yPos, flags, param):
    global draw, p1, p2
    
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        p1 = (xPos, yPos)
        p2 = p1
    elif event == cv2.EVENT_MOUSEMOVE and draw:
        p2 = (xPos, yPos)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        crop_and_save(p1, p2)

def crop_and_save(start_point, end_point):
    x1, y1 = start_point
    x2, y2 = end_point
    
    # Ensure the correct order of coordinates
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    
    # Crop the image
    cropped = frame[y1:y2, x1:x2]
    
    # Save the cropped image
    cv2.imwrite("./task_4/cropped_image.jpg", cropped)
    print("Cropped image saved as 'cropped_image.jpg'")

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouseClick)
frame = cv2.imread("./task_4/tom.jpg")
while True:
    img = frame.copy()
    if draw:
        cv2.rectangle(img, p1, p2, (0, 255, 0), 2)
    cv2.imshow("Image", img)
    
    cv2.waitKey()
    break
img2 = cv2.imread("./task_4/cropped_image.jpg")
cv2.imshow("Cropped Image", img2)
cv2.waitKey()
cv2.destroyAllWindows()