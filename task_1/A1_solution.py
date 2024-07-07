import cv2
import numpy as np

path1 = "./task_1/tom.jpg"
path2 = "./task_1/rdj.jpg"

image_1 = cv2.imread(path1)
image_2 = cv2.imread(path2)

# Ensure both images have the same height
max_height = min(image_1.shape[0], image_2.shape[0])
image_1 = cv2.resize(image_1, (int(image_1.shape[1] * max_height / image_1.shape[0]), max_height))
image_2 = cv2.resize(image_2, (int(image_2.shape[1] * max_height / image_2.shape[0]), max_height))

new_image = cv2.hconcat([image_1, image_2])

image_gray = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
image_gray_3channel = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)

final_image = cv2.vconcat([new_image, image_gray_3channel])

cv2.imshow("Output", final_image)
cv2.imwrite('./task_1/A1_solution.jpg', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()