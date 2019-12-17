"""
cv2.medianBlur()
関数はカーネル内の全画素の中央値を計算します．
ごま塩ノイズのようなノイズに対して効果的です．
箱型フィルタとガウシアンフィルタの出力結果は原画像中には存在しない画素値を出力とするのに対して，
中央値フィルタの出力は常に原画像中から選ばれています．
そのためごま塩ノイズのような特異なノイズに対して効果的です．
カーネルサイズは奇数でなければいけません．
"""

import cv2
import numpy as np


FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

#kernel size
k = 5

median = cv2.medianBlur(src_img,5)

cv2.imshow('source', src_img)
cv2.imshow('median', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
