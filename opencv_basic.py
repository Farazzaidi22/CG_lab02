import cv2

#to display img in the form of a 2D matrix
#image address bhi dal skte hain direct (eg:- C:\\Users\\Faraz_0hm6\\OneDrive\\Desktop\\basketball.png)
img = cv2.imread("lena.jpg", -1) # 0= grayscale, 1= RGB, -1= alpha shaders
print(img)

cv2.imshow("image", img) #to display image

#how long window should be displayed (in nano seconds i.e 5 sec = 5000)
cv2.waitKey(0) # just like Waitforseconds in unity func (0 is for running it infinitly)
cv2.destroyAllWindows()

#to copy an image
cv2.imwrite("lena.jpg", img)
