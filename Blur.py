import cv2
import numpy as np


FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

#kernel size
k = 5

kernel = np.ones((k,k),np.float32) / 25
# blur = cv2.blur(src_img,(5,5)) 
dst_img = cv2.filter2D(src_img,-1,kernel)

cv2.imshow('source', src_img)
cv2.imshow('median', dst_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
