import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#uint8 is an unsigned 8-bit integer that can represent values 0..255
#numpy uint8 will wrap. For example, 235+30 = 9
#img = np.zeros((200,200), np.uint8)

img =cv.imread("lena.jpg")

cv.imshow("img", img)

#splitting img in RGB 
b,r,g = cv.split(img)

cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

#hist(array, no of pixels, range of those pixels)
#ravel is used for flattening a 2D array into 1D
plt.hist(img.ravel(), 256, [0,256]) 

plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()