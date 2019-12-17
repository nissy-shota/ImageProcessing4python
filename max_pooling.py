"""
ここでは平均値でなく最大値でプーリングせよ。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

max_pooling_img = np.zeros_like(src_img)

Height,Width,Channel = src_img.shape

for y in range(0,Height,8):
    for x in range(0,Width,8):
        for c in range(Channel):
            kernel = src_img[y:y+8,x:x+8,c]
            max = np.max(kernel)
            max_pooling_img[y:y + 8, x:x + 8, c] = max
max_pooling_img = max_pooling_img.astype(np.uint8)

cv2.imshow('max Pooling', max_pooling_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

