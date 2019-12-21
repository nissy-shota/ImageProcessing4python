"""
Histogram normalization
ヒストグラム正規化を実装せよ。
ヒストグラムは偏りを持っていることが伺える。
例えば、0に近い画素が多ければ画像は全体的に暗く、255に近い画素が多ければ画像は明るくなる。
ヒストグラムが局所的に偏っていることをダイナミックレンジが狭いなどと表現する。
そのため画像を人の目に見やすくするために、ヒストグラムを正規化したり平坦化したりなどの処理が必要である。
このヒストグラム正規化は濃度階調変換(gray-scale transformation) と呼ばれ、
[c,d]の画素値を持つ画像を[a,b]のレンジに変換する場合は次式で実現できる。
今回はimori_dark.jpgを[0, 255]のレンジにそれぞれ変換する。
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


# histogram normalization
def hist_normalization(img, a=0, b=255):
    # get max and min
    c = img.min()
    d = img.max()

    out = img.copy()
    # normalization
    out = (b - a) / (d - c) * (out - c) + a
    out[out < a] = a
    out[out > b] = b
    out = out.astype(np.uint8)

    return out


# Read image
img = cv2.imread("imori_dark.jpg").astype(np.float32)
# out2 = np.clip(img,0,255).astype(np.uint8)
# histogram normalization
out = hist_normalization(img)

# Display histogram
plt.hist(out.ravel(), bins=255, rwidth=0.8, range=(0, 255))
plt.hist(img.ravel(), bins=255, rwidth=0.8, range=(0, 255))

plt.show()
# Save result
cv2.imshow("result", out)

cv2.waitKey(0)
cv2.destroyAllWindows()