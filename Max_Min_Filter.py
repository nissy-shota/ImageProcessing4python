"""
MAX-MINフィルタとはフィルタ内の画素の最大値と最小値の差を出力するフィルタであり、
エッジ検出のフィルタの一つである。
エッジ検出とは画像内の線を検出るすることであり、
このような画像内の情報を抜き出す操作を特徴抽出と呼ぶ。
エッジ検出では多くの場合、グレースケール画像に対してフィルタリングを行う。
"""

import cv2
import numpy as np

def max_min_filter(img,k_size):

    H,W = img.shape
    #padding
    pad = k_size // 2
    padding_img = np.zeros((H + pad * 2, W + pad * 2), dtype= np.float32)
    padding_img[pad:pad+H,pad:pad+W] = img.copy().astype(np.float32)
    dst = padding_img.copy()

    """
    np.max(padding_img[y:y+k_size,x:x+k_size]) - np.min(padding_img[y:y+k_size,x:x+k_size])
    ここは，pad + y + k_size でなくていい．なぜならPaddingしたから．
    y＋k_sizeとすると端のゼロまで含まれてしまうが，それは仕方のないことである．
    """
    for y in range(H):
        for x in range(W):
            dst[pad+y, pad+x] = np.max(padding_img[y:y+k_size,x:x+k_size]) - np.min(padding_img[y:y+k_size,x:x+k_size])

    dst = dst[pad: pad + H, pad: pad + W].astype(np.uint8)

    return dst



FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)
gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

dst_img = max_min_filter(gray,3)

cv2.imshow('source', src_img)
cv2.imshow('max-min filter', dst_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

