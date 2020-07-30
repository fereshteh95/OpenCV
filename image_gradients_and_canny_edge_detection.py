import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv/samples/data/sudoku.png', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))
sobelCombined = cv.bitwise_or(sobelX, sobelY)

titles = ['image', 'lap', 'sobelX', 'sobelY', 'combined']
images = [img, lap, sobelX, sobelY, sobelCombined]
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