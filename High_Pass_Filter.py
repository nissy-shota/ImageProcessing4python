import cv2
import numpy as np
import matplotlib.pyplot as plt

src_img = cv2.imread('asuka.jpg')
gray = cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)

fourier_img = np.fft.fft2(gray)
fourier_img = np.fft.fftshift(fourier_img)

H,W = gray.shape
centerx = int(W/2)
centery = int(H/2)

mask = np.zeros_like(gray)
R = 50
for x in range(0,W):
    for y in range(0,H):
        if (x- centery)**2 +(y- centery)**2>R**2:
            mask[x,y]=1

# mask = 255- mask
tmp = mask * 255
cv2.imshow('mask',tmp)

print(mask)
fourier_img *= mask
fourier_img = np.fft.fftshift(fourier_img)
ifimg = np.fft.ifft2(fourier_img)
ifimg = np.uint8(ifimg.real)


cv2.imshow('lp',ifimg)
cv2.waitKey()
cv2.destroyAllWindows()