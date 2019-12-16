"""
大津の二値化を実装せよ。 大津の二値化とは判別分析法と呼ばれ、
二値化における分離の閾値を自動決定する手法である。
これはクラス内分散とクラス間分散の比から計算される。

グレースケールの輝度値（ピクセルの値）のヒストグラムはこうなる。

二値化はある値を境界にして、０か１にする方法だけど、

閾値t未満をクラス0, t以上をクラス1とする。
w0, w1 ... 閾値tにより分離された各クラスの画素数の割合 (w0 + w1 = 1を満たす)
S0^2, S1^2 ... 各クラスの画素値の分散
M0, M1 ... 各クラスの画素値の平均値
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Otsu Binalization

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH, cv2.IMREAD_GRAYSCALE)
gray = src_img.copy()
ret, Bin = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

#######################################
"""
cf:
flatten関数は、元々のリストのコピーを常に返します。
一方、ravel関数は、元々のリストの見た目のみを変えて返すため返されたリストの要素を変更すると、
元々のリストまで変わってしまうことがあり、注意が必要です。
"""

gray_img = 0.2126 * src_img[..., 2] + 0.7152 * src_img[..., 1] + 0.0722 * src_img[..., 0]
plt.hist(gray_img.ravel(order='C'), bins=255, rwidth=0.8, range=(0, 255))
plt.xlabel('value')
plt.ylabel('appearance')
plt.show()

########################################
# display
print(f'this process\'s threshold is {ret}')
H,W = gray.shape[:2]
print(f'Height is {H}. Width is {W}')

cv2.imshow('src_img', src_img)
cv2.imshow('OTSU_Binaryzation', Bin)


cv2.waitKey(0)
cv2.destroyAllWindows()