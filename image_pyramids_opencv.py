import cv2 as cv
import numpy as np

img = cv.imread('opencv/samples/data/lena.jpg')
# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)
# hr1 = cv.pyrUp(lr2)
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    cv.imshow(str(i), layer)

cv.imshow('original image', img)
# cv.imshow('pyrDown 1', lr1)
# cv.imshow('pyrDown 2', lr2)
# cv.imshow('pyrUp 1', hr1)
cv.waitKey(0)
cv.destroyAllWindows()
