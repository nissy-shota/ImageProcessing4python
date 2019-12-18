"""
Prewittフィルタ(3x3)を実装せよ。
Prewittフィルタはエッジ抽出フィルタの一種であり、次式で定義される。
Prewitt(プレヴィット)は、画像から輪郭を抽出する空間フィルタの1つです。
このフィルタは、同様に輪郭検出を行う一次微分フィルタをノイズの影響を受けにくいように、平滑化処理を加えて改良したものです。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

vertical_kernel = np.array([[-1,-1,-1],
                            [0,0,0],
                            [1,1,1]])

horizonal_kernel = np.array([[-1,0,1],
                             [-1,0,1],
                             [-1,0,1]])

gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

dst1 = cv2.filter2D(gray,-1,vertical_kernel)
dst2 = cv2.filter2D(gray,-1,horizonal_kernel)

gray_x = cv2.filter2D(gray, cv2.CV_64F, horizonal_kernel)
gray_y = cv2.filter2D(gray, cv2.CV_64F, vertical_kernel)

dst = np.sqrt(gray_x ** 2 + gray_y ** 2)
dst = dst.astype(np.uint8)



cv2.imshow('source', src_img)
cv2.imshow('prewitt filter vertical', dst1)
cv2.imshow('prewitt filter horizonal', dst2)
cv2.imshow('prewitt', dst)
# cv2.imwrite("kannnax.jpg",sobelx)
# cv2.imwrite("kannnay.jpg",sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()


