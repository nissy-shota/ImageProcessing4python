"""
画像をグレースケールにせよ。 グレースケールとは、画像の輝度表現方法の一種であり下式で計算される。
Y = 0.2126 R + 0.7152 G + 0.0722 B
"""

import numpy as np
import cv2

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)

# convert grayscale expression
# Y = 0.2126 R + 0.7152 G + 0.0722 B
myGray = src_img[:,:,0] * 0.0722 + src_img[:,:,1] * 0.7152 + src_img[:,:,2] * 0.2126
myGray = myGray.astype(np.uint8)


########################################
# display
cv2.imshow('src_img', src_img)
cv2.imshow('Gray (Using cvtColor function)', gray)
cv2.imshow('Gray (Using convert gray image expression.)', myGray)

cv2.waitKey(0)
cv2.destroyAllWindows()