import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv/samples/data/lena.jpg', cv.IMREAD_GRAYSCALE)
canny = cv.Canny(img, 100, 200)


titles = ['image', 'canny']
images = [img, canny]
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