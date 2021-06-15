import sys
import numpy as np
import cv2

#바로 가우시안블러------------------------------------------------
src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


blr = cv2.GaussianBlur(src, (0, 0), 2)
dst = np.clip(2*src - blr, 0, 255)
print(dst)

# 실수로 변환 후 가우시안블러---------------------------------------
src_1 = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src_1 is None:
    print('Image load failed!')
    sys.exit()

src_f = src_1.astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
dst_f = np.clip(2.0*src_f - blr, 0, 255).astype(np.uint8)

#출력----------------------------------------------------------------
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst_f', dst_f)
cv2.waitKey()

cv2.destroyAllWindows()
