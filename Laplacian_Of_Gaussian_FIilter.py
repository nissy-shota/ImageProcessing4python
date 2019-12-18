"""
LoGフィルタ(sigma=3、カーネルサイズ=5)を実装し、
imori_noise.jpgのエッジを検出せよ。
LoGフィルタとはLaplacian of Gaussianであり、
ガウシアンフィルタで画像を平滑化した後にラプラシアンフィルタで輪郭を取り出すフィルタである。
Laplcianフィルタは二次微分をとるのでノイズが強調されるのを防ぐために、
予めGaussianフィルタでノイズを抑える。
LoGフィルタは次式で定義される。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)
kernel_size = (3,3)
#gasussian filter
Gaussian_img = cv2.GaussianBlur(src_img,ksize=kernel_size,sigmaX=1.3)
LoG_img = cv2.Laplacian(Gaussian_img, -1, ksize=3)
LoG_img = LoG_img.astype(np.float32)
cv2.imshow("LoG Filter",LoG_img)

cv2.waitKey(0)
cv2.destroyAllWindows()