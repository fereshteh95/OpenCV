import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('opencv/samples/data/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateral = cv.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2d CONV', 'blur', 'gblur', "median", 'bilateral']
images = [img, dst, blur, gblur, median, bilateral]
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