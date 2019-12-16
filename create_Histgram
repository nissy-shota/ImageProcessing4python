import cv2
import matplotlib.pyplot as plt

FILE_PATH = "HashimotoKanna.jpg"
src_img = cv2.imread(FILE_PATH, cv2.IMREAD_GRAYSCALE)

gray_img = 0.2126 * src_img[..., 2] + 0.7152 * src_img[..., 1] + 0.0722 * src_img[..., 0]
plt.hist(gray_img.ravel(order='C'), bins=255, rwidth=0.8, range=(0, 255))
plt.xlabel('value')
plt.ylabel('appearance')
plt.show()