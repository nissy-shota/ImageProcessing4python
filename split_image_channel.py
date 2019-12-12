import cv2
import numpy as np

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH)

blue = src_img[:, :, 0].copy()
green = src_img[:, :, 1].copy()
red = src_img[:, :, 2].copy()


inverse_img = cv2.imread(FILE_PATH)[:,:,::-1]

cv2.imshow('source image', src_img)

cv2.imshow('blue component', blue)
cv2.imshow('green component', green)
cv2.imshow('red component', red)

cv2.waitKey(0)
cv2.destroyAllWindows()
