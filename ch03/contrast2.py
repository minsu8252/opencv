import sys
import numpy as np
import cv2
import histogram_test as test

src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()


dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

#made_functions
# gmin= np.min(src)
# gmax= np.max(src)
# dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8) #numpy사용 동일 결과

#히스토그램
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = test.getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)
cv2.waitKey()

cv2.destroyAllWindows()
