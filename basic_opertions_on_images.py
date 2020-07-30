import numpy as np
import cv2

img = cv2.imread('opencv/samples/data/messi5.jpg')
img2 = cv2.imread('opencv/samples/data/opencv-logo.png')

print(img.shape)  # (rows, columns, channels)
print(img.size)  # total num of pixels
print(img.dtype)  # image dtype
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
# new_img = cv2.add(img2, img)
new_img = cv2.addWeighted(img, 0.8, img2, 0.2, 0)

cv2.imshow('image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
