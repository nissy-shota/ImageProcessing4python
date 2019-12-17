"""
ガウシアンフィルタ(3x3、標準偏差1.3)を実装し、imori_noise.jpgのノイズを除去せよ。
ガウシアンフィルタとは画像の平滑化（滑らかにする）を行うフィルタの一種であり、ノイズ除去にも使われる。
ノイズ除去には他にも、メディアンフィルタ(Q.10)、平滑化フィルタ(Q.11)、LoGフィルタ(Q.19)などがある。
ガウシアンフィルタは注目画素の周辺画素を、ガウス分布による重み付けで平滑化し、次式で定義される。
このような重みはカーネルやフィルタと呼ばれる。
ただし、画像の端はこのままではフィルタリングできないため、画素が足りない部分は0で埋める。
これを0パディングと呼ぶ。 かつ、重みは正規化する。(sum g = 1)
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

kernel_size = (3,3)
#gasussian filter
Gaussian_img = cv2.GaussianBlur(src_img,ksize=kernel_size,sigmaX=1.3)



cv2.imshow('source', src_img)
cv2.imshow('Gaussian', Gaussian_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
