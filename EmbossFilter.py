"""
Embossフィルタを実装せよ。
Embossフィルタとは輪郭部分を浮き出しにするフィルタで、次式で定義される。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

Emboss_kernel = np.array([[-2,-1,0],
                            [-1,1,1],
                            [0,1,2]])
gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

dst = cv2.filter2D(gray,-1,Emboss_kernel)
dst = dst.astype(np.uint8)

cv2.imshow('source', src_img)
cv2.imshow('Emboss', dst)
# cv2.imwrite("kannnax.jpg",sobelx)
# cv2.imwrite("kannnay.jpg",sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()


