import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg", 1)

hist = cv.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()