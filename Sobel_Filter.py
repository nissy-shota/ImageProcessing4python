"""
Prewittフィルタ(3x3)を実装せよ。
Prewittフィルタはエッジ抽出フィルタの一種であり、次式で定義される。
プレウィットフィルタは「平滑化フィルタ」と「微分フィルタ」を組み合わせることで、ノイズの影響を抑えながら輪郭を抽出します。
その平滑化フィルタをかける際に「注目画素との距離に応じて重み付けを変化させた」ものがソーベルフィルタです。
これにより自然に平滑化を行うことが出来ます。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

vertical_kernel = np.array([[1,2,1],
                            [0,0,0],
                            [-1,-2,-1]])

horizonal_kernel = np.array([[1,0,-1],
                             [2,0,-2],
                             [1,0,-1]])

gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

dst1 = cv2.filter2D(gray,-1,vertical_kernel)
dst2 = cv2.filter2D(gray,-1,horizonal_kernel)

sobelx = cv2.Sobel(gray, -1, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, -1, 0, 1, ksize=3)


cv2.imshow('source', src_img)
cv2.imshow('Sobel filter vertical', dst1)
cv2.imshow('Sobel filter horizonal', dst2)
cv2.imshow('Sobel filter vertical opencv', sobelx)
cv2.imshow('Sobel filter horizonal opencv', sobely)

# cv2.imwrite("kannnax.jpg",sobelx)
# cv2.imwrite("kannnay.jpg",sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()


