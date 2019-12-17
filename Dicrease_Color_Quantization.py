"""
ここでは画像の値を256^3から4^3、すなわちR,G,B in {32, 96, 160, 224}の各4値に減色せよ。
これは量子化操作である。 各値に関して、以下の様に定義する。
"""
import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

quantization_table = [32,96,160,224]

dicrease_color_img = src_img.copy()
#64は公差　Dicreaseは公差で切り捨て除算をおこない，初項をを加えれば良い．dst = src//d * d + a0
# broad cast がおきているため，すべてに割り算が適応される．
dicrease_color_img = dicrease_color_img // 64 * 64 + 32
cv2.imshow('dicrease_color', dicrease_color_img)




cv2.waitKey(0)
cv2.destroyAllWindows()
