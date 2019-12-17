"""
HSV変換を実装して、色相Hを反転せよ。
HSV変換とは、Hue(色相)、Saturation(彩度)、Value(明度) で色を表現する手法である。

Hue ... 色合いを0~360度で表現し、赤や青など色の種類を示す。 ( 0 <= H < 360) 色相は次の色に対応する。
Saturation ... 色の鮮やかさ。Saturationが低いと灰色さが顕著になり、くすんだ色となる。 ( 0<= S < 1)
Value ... 色の明るさ。Valueが高いほど白に近く、Valueが低いほど黒に近くなる。 ( 0 <= V < 1)

"""
import numpy as np
import cv2

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)
hsv =  cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)

hue = hsv[...,0]
sarturation = hsv[...,1]
value = hsv[...,2]

########################################
# display


cv2.imshow('src_img', src_img)
cv2.imshow('HSV', hsv)
cv2.imshow('Hue', hue)
cv2.imshow('Sarturation', sarturation)
cv2.imshow('Value', value)


cv2.waitKey(0)
cv2.destroyAllWindows()