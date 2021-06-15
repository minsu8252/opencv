import sys
import numpy as np
import cv2


# 그레이스케일 영상의 히스토그램 평활화-------------------------------
src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 컬러 영상의 히스토그램 평활화---------------------------------------
src = cv2.imread('field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb)


# 밝기 성분에 대해서만 히스토그램 평활화 수행
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0])

dst_ycrcb = cv2.merge(ycrcb_planes)

dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)
# YCrCd는 바로 출력이 안되기 때문에 BGR로 변환
cv2.imshow('src', src)
cv2.imshow('dst', dst_ycrcb)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()

# BGR로 바로 실행-----------------------------------------------------
src = cv2.imread('field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

src_planes = cv2.split(src)
src_planes[0] = cv2.equalizeHist(src_planes[0])
src_planes[1] = cv2.equalizeHist(src_planes[1])
src_planes[2] = cv2.equalizeHist(src_planes[2])
src_1 = cv2.merge(src_planes)

cv2.imshow('src', src)
cv2.imshow('src_1', src_1)
cv2.waitKey()
cv2.destroyAllWindows()
