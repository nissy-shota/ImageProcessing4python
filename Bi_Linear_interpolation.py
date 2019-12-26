import cv2
import numpy as np

def bi_linear_interpolation(img,ax=1.,ay=1.):
    H, W, C = img.shape

    aH = int(ay * H)
    aW = int(ax * W)

    # get position of resized image
    y = np.arange(aH).repeat(aW).reshape(aH, -1)
    x = np.tile(np.arange(aW), (aH, 1))

    # get position of original position
    y = (y / ay)
    x = (x / ax)

    ix = np.floor(x).astype(np.int)
    iy = np.floor(y).astype(np.int)

    ix = np.minimum(ix,W-2)
    iy = np.minimum(iy,H-2)
    # get distance
    dx = x - ix
    dy = y - iy

    dx = np.repeat(np.expand_dims(dx, axis=-1), 3, axis=-1)
    dy = np.repeat(np.expand_dims(dy, axis=-1), 3, axis=-1)

    # interpolation
    out = (1 - dx) * (1 - dy) * img[iy, ix] + dx * (1 - dy) * img[iy, ix + 1] + (1 - dx) * dy * img[
        iy + 1, ix] + dx * dy * img[iy + 1, ix + 1]

    out = np.clip(out, 0, 255)
    out = out.astype(np.uint8)

    return out

src_img = cv2.imread('HashimotoKanna.jpg').astype(np.float32)
# Bilinear interpolation
out = bi_linear_interpolation(src_img, ax=1.5, ay=1.5)

cv2.imshow('source image.',src_img)
cv2.imshow('out image',out)
cv2.waitKey(0)
cv2.destroyAllWindows()