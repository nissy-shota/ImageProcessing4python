"""
ガンマ補正とは、カメラなどの媒体の経由によって画素値が非線形的に変換された場合の補正である。
ディスプレイなどで画像をそのまま表示すると画面が暗くなってしまうため、RGBの値を予め大きくすることで、
ディスプレイの特性を排除した画像表示を行うことがガンマ補正の目的である。
非線形変換は次式で起こるとされる。 ただしxは[0,1]に正規化されている。 c ... 定数、g ... ガンマ特性(通常は2.2)
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


# gamma correction
def gamma_correction(img, c=1, g=2.2):
	out = img.copy()
	out /= 255.
	out = (1/c * out) ** (1/g)
	out *= 255
	out = out.astype(np.uint8)
	return out

# Read image
img = cv2.imread("imori_dark.jpg").astype(np.float32)

# Gammma correction
out = gamma_correction(img)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)