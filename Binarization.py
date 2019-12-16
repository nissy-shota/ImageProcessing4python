"""
画像を二値化せよ。 二値化とは、画像を黒と白の二値で表現する方法である。
ここでは、グレースケールにおいて閾値を128に設定し、下式で二値化する。

y = { 0 (if y < 128)
     255 (else)
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH, cv2.IMREAD_GRAYSCALE)


# numpy
threshold = 128
myBin = src_img.copy()
myBin[myBin > threshold] = 255
myBin[myBin < threshold] = 0
# OpenCV
ret,Bin = cv2.threshold(src_img,127,255,cv2.THRESH_BINARY)



##############################
#display
cv2.imshow('src_img', src_img)
cv2.imshow('Binarization(numpy)', myBin)
cv2.imshow('Binarization(OpenCV)', myBin)
print(f' retvalue is threshold. this processs threshold is  {ret}')

cv2.waitKey(0)
cv2.destroyAllWindows()