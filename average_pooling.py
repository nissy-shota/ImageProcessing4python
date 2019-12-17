"""
ここでは画像をグリッド分割(ある固定長の領域に分ける)し、かく領域内(セル)の平均値でその領域内の値を埋める。
このようにグリッド分割し、その領域内の代表値を求める操作はPooling(プーリング) と呼ばれる。
これらプーリング操作はCNN(Convolutional Neural Network) において重要な役割を持つ。

v = 1/|R| * Sum_{i in R} v_i
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

pooling_img = np.zeros_like(src_img)

Height,Width,Channel = src_img.shape

for y in range(0,Height,8):
    for x in range(0,Width,8):
        for c in range(Channel):
            kernel = src_img[y:y+8,x:x+8,c]
            mean = np.mean(kernel)
            pooling_img[y:y + 8, x:x + 8, c] = mean
pooling_img = pooling_img.astype(np.uint8)

cv2.imshow('Pooling image', pooling_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

