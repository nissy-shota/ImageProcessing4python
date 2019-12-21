"""
ヒストグラムの平均値をm0=128、標準偏差をs0=52になるように操作せよ。
これはヒストグラムのダイナミックレンジを変更するのではなく、ヒストグラムを平坦に変更する操作である。
平均値m、標準偏差s、のヒストグラムを平均値m0, 標準偏差s0に変更するには、次式によって変換する。
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
def change_mean_std(img,mean=128,std=52):
    m = np.mean(img)
    s = np.std(img)

    dst = img.copy()
    dst = std / s * (dst - m) + mean
    dst[dst<0] = 0
    dst[dst>255] = 255

    dst = dst.astype(np.uint8)
    return dst

src_img = cv2.imread("imori_dark.jpg").astype(np.float32)
dst = change_mean_std(src_img)

plt.hist(dst.ravel(),bins=255,rwidth=0.8,range=(0,255))
plt.show()
src = src_img.astype(np.uint8)
cv2.imshow("result",dst)
cv2.imshow("src",src)

cv2.waitKey(0)
cv2.destroyAllWindows()
