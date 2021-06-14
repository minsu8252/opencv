import numpy as np
import cv2


def on_level_change(pos):
    global img
    #getTrackbarpos(트랙바 이름, 윈도우창 이름)
    r= cv2.getTrackbarPos('R', 'image')
    g= cv2.getTrackbarPos('G', 'image')
    b= cv2.getTrackbarPos('B', 'image')

    img[:] = (b, g, r)
    cv2.imshow('image', img)

# 출력 창 크기 설정 
# zeros((세로, 가로, RGB이면 3), np.uint8)
img = np.zeros((300, 600, 3), np.uint8)
# 윈도우 창 이름
cv2.namedWindow('image')
# (트랙바이름, 윈도우 창 이름, 최소값, 최대값, 콜백 함수)
# 윈도우 창 이름이 같아야 트랙바를 넣을 수 있다.
cv2.createTrackbar('R', 'image', 0, 255, on_level_change)
cv2.createTrackbar('G', 'image', 0, 255, on_level_change)
cv2.createTrackbar('B', 'image', 0, 255, on_level_change)

# 실행 및 끄기 설정
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()