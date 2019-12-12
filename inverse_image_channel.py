"""
画像を読み込み、RGBをBGRの順に入れ替えよ。

画像の赤成分を取り出すには、以下のコードで可能。
cv2.imread()関数ではチャネルがBGRの順になることに注意！
これで変数redにimori.jpgの赤成分のみが入る。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

blue = src_img[:, :, 0].copy()
green = src_img[:, :, 1].copy()
red = src_img[:, :, 2].copy()


inverse_img = cv2.imread(FILE_PATH)[:,:,::-1]

cv2.imshow('source image', src_img)

cv2.imshow('blue component', blue)
cv2.imshow('green component', green)
cv2.imshow('red component', red)

cv2.imshow('inversement image', inverse_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
