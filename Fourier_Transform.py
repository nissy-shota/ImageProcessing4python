import cv2
import numpy as np
import matplotlib.pyplot as plt

src_img = cv2.imread('asuka.jpg')
gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

fourier_img = np.fft.fft2(gray)
fourier_img = np.fft.fftshift(fourier_img)
mag = 20 * np.log(np.abs(fourier_img))


plt.figure(figsize=(20,6))
plt.subplot(131)
plt.imshow(gray, cmap='gray')
plt.subplot(132)
plt.imshow(mag, cmap='gray')
fourier_img = np.fft.fftshift(fourier_img)
ifimg = np.fft.ifft2(fourier_img)
ifimg = np.uint8(ifimg.real)
plt.subplot(133)
plt.imshow(ifimg, cmap='gray')

plt.show()


