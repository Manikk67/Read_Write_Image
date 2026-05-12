import cv2
import numpy

img=cv2.imread("C:\\Users\\KOTTAIMANI\\OneDrive\\Documents\\AI-NOVITECH\\demopic.jpg")
cv2.imshow('show',img)
cv2.imwrite('newimage.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

