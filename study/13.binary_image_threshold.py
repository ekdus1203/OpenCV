import cv2


src = cv2.imread("../img/cameraman.jpg", cv2.IMREAD_GRAYSCALE)

# _, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)
_, binary = cv2.threshold(src, 64, 255, cv2.THRESH_BINARY)

cv2.namedWindow("binary")
dst = cv2.resize(binary, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.imshow("binary", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()