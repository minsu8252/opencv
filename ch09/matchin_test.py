import sys
import cv2
import numpy as np

src1 = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('img2.jpg', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('사진없음')
    sys.exit()


feature = cv2.KAZE_create()

kp1, desc1 = feature.detectAndCompute(src1, None)
kp2, desc2 = feature.detectAndCompute(src2, None)

matcher = cv2.BFMatcher_create()
matches = matcher.match(desc1, desc2)

dst = cv2.drawMatches(src1, kp1, src2, kp2, matches, None)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()