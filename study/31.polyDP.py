import cv2

src = cv2.imread("../img/chess.png")
cv2.imshow("src", src)
cv2.waitKey(0)
dst = src.copy()

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)
ret, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", binary)
cv2.waitKey(0)
morp = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)
cv2.imshow("morp", morp)
cv2.waitKey(0)
image = cv2.bitwise_not(morp)
cv2.imshow("bitwise_not", image)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for i in contours:
    perimeter = cv2.arcLength(i, True)
    epsilon = perimeter * 0.05
    approx = cv2.approxPolyDP(i, epsilon, True)
    cv2.drawContours(dst, [approx], 0, (0, 0, 255), 3)
    for j in approx:
        cv2.circle(dst, tuple(j[0]), 3, (255, 0, 0), -1)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()