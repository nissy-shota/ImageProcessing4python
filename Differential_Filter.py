"""
微分フィルタ(3x3)を実装せよ。
微分フィルタは輝度の急激な変化が起こっている部分のエッジを取り出すフィルタであり、
隣り合う画素同士の差を取る。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

vertical_kernel = np.array([[0,-1,0],
                            [0,0,0],
                            [0,1,0]])

horizonal_kernel = np.array([[0,0,0],
                             [-1,0,1],
                             [0,0,0]])

gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

dst1 = cv2.filter2D(gray,-1,vertical_kernel)
dst2 = cv2.filter2D(gray,-1,horizonal_kernel)


cv2.imshow('source', src_img)
cv2.imshow('Differential filter vertical', dst1)
cv2.imshow('Differential filter horizonal', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()


