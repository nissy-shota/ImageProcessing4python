"""
Laplacianフィルタを実装せよ。
Laplacian（ラプラシアン）フィルタとは輝度の二次微分をとることでエッジ検出を行うフィルタである。
"""

import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

Laplacian_kernel = np.array([[0,1,0],
                            [1,-4,1],
                            [0,1,0]])



gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

dst = cv2.filter2D(gray,-1,Laplacian_kernel)
dst = dst.astype(np.uint8)

dst1 = cv2.Laplacian(gray, -1, ksize=3)



cv2.imshow('source', src_img)
cv2.imshow('Laplacian', dst)
cv2.imshow('Laplacian opencv', dst1)
# cv2.imwrite("kannnax.jpg",sobelx)
# cv2.imwrite("kannnay.jpg",sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()


