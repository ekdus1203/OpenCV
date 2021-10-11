import cv2

src = cv2.imread("prelabel.PNG", cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
dst_erode = cv2.erode(binary, kernel, iterations=5)
dst_dilate = cv2.dilate(dst_erode, kernel, iterations=9)
result = cv2.erode(dst_dilate, kernel, iterations=4)

# src = cv2.pyrDown(src)
# dst_dilate = cv2.pyrDown(dst_dilate)
# dst_erode = cv2.pyrDown(dst_erode)


cv2.imshow("src", src)
cv2.imshow("dst_dilate", dst_dilate)
cv2.imshow("dst_erode", dst_erode)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()