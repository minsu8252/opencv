import sys
import cv2
import numpy as np

src = cv2.imread('tekapo.bmp')

if src is None:
    print('사진 없음')
    sys.exit()

src_1=cv2.flip(src, flipCode=1, dst=None)
src_2=cv2.flip(src, flipCode=0, dst=None)
src_3=cv2.flip(src, flipCode=-1, dst=None)

cv2.imshow('src', src)
cv2.imshow('src_1', src_1)
cv2.imshow('src_2', src_2)
cv2.imshow('src_3', src_3)
cv2.waitKey()
cv2.destroyAllWindows()