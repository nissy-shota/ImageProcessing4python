"""
モーションフィルタ(3x3)を実装せよ。
モーションフィルタとは対角方向の平均値を取るフィルタであり、次式で定義される。
"""

import numpy as np
import cv2

def motion_filter(img,kernel_size):
    kernel = np.diag([1] * kernel_size).astype(np.float32)
    kernel /= kernel_size

    # #padding
    # h,w,c = img.shape
    # pad = kernel_size//2
    # dst = np.zeros((h+pad*2,w+pad*2,c),dtype=np.float32)
    # dst[pad:pad+h,pad:pad+w] = img.copy().astype(np.float32)
    #
    # tmp = dst.copy()
    #
    # # filtering
    # for y in range(h):
    #     for x in range(w):
    #         for c in range(c):
    #             dst[pad + y, pad + x, c] = np.sum(kernel * tmp[y: y + kernel_size, x: x + kernel_size, c])
    #
    # dst = dst[pad: pad + h, pad: pad + w].astype(np.uint8)

    dst = cv2.filter2D(img,-1,kernel)
    return dst

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

dst_img = motion_filter(src_img,10)

cv2.imshow('source', src_img)
cv2.imshow('motion filter', dst_img)

cv2.waitKey(0)
cv2.destroyAllWindows()