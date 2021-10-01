import cv2

# color 이미지를 binary로 하면 각 rab 채널별로 binary한 후 합쳐진 것
# 그래서 color 이미지는 binary하지 않는다
# src = cv2.imread("../img/swan.jpg)

src = cv2.imread('../img/cameraman.jpg',cv2.IMREAD_GRAYSCALE)

#자동으로 임계값을 찾아주는 알고리즘
#_, binary= cv2.threshold(src, 647,255,cv2.THRESH_BINARY)
_, binary= cv2.threshold(src, -1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.namedWindow("binary")
dst= cv2.resize(binary,dsize=(640,480),interpolation=cv2.INTER_AREA)
cv2.imshow("binary",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()