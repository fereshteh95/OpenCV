import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv/samples/data/smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilation = cv.dilate(mask, kernel=kernel, iterations=2)
erosion = cv.erode(mask, kernel=kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel=kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel=kernel)


titles = ['image', 'mask', 'dilation', 'erosion', 'open', 'close']
images = [img, mask, dilation, erosion, opening, closing]
n = len(images)

for i in range(n):
    if n <= 4:
        if n % 2 == 0:
            plt.subplot(2, n/2, i+1)
        else:
            plt.subplot(1, n, i+1)
    else:
        if n % 2 == 0:
            plt.subplot(2, n/2, i+1)
        else:
            plt.subplot(2, np.floor(n/2)+1, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
