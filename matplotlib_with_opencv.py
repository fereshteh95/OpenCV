import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('opencv/samples/data/lena.jpg')
cv.imshow('Image', img)

img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img2)
# plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

