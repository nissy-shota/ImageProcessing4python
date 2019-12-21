"""
最近傍補間により画像を1.5倍に拡大せよ。
最近傍補間(Nearest Neighbor)は画像の拡大時に最近傍にある画素をそのまま使う手法である。
シンプルで処理速度が速いが、画質の劣化は著しい。
次式で補間される。 I' ... 拡大後の画像、 I ... 拡大前の画像、a ... 拡大率、[ ] ... 四捨五入
"""
import cv2
import numpy as np
# Nereset Neighbor interpolation
def nn_interpolate(img, ax=1, ay=1):

	H, W, C = img.shape

	aH = int(ay * H)
	aW = int(ax * W)

	y = np.arange(aH).repeat(aW).reshape(aH, -1)
	x = np.tile(np.arange(aW), (aH, 1))
	y = np.round(y / ay).astype(np.int)
	x = np.round(x / ax).astype(np.int)

	out = img[y,x]

	out = out.astype(np.uint8)

	return out


# Read image
img = cv2.imread("imori_dark.jpg").astype(np.float)

# Nearest Neighbor
out = nn_interpolate(img, ax=1.5, ay=1.5)

# Save result
cv2.imshow("result", out)
cv2.waitKey(0)