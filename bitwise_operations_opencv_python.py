import cv2
import numpy as np

img1 = np.zeros((384, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = cv2.imread('opencv/samples/data/home.jpg')

# bitImg = cv2.bitwise_and(img2, img1)
# bitImg = cv2.bitwise_or(img2, img1)
# bitImg = cv2.bitwise_xor(img1, img2)
bitImg = cv2.bitwise_not(img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitImg', bitImg)

cv2.waitKey(0)
cv2.destroyAllWindows()