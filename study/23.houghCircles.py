import cv2

src = cv2.imread("../img/colorball.png")
cv2.imshow("src", src);cv2.waitKey(0);cv2.destroyWindow("src")
dst = src.copy()

image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", image);cv2.waitKey(0);cv2.destroyWindow("gray")

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
morp = cv2.erode(image, kernel, iterations=5)
cv2.imshow("erode", morp);cv2.waitKey(0);cv2.destroyWindow("erode")
morp = cv2.dilate(morp, kernel, iterations=5)
cv2.imshow("dilate", morp);cv2.waitKey(0);cv2.destroyWindow("dilate")
morp = cv2.dilate(morp, kernel, iterations=3)
cv2.imshow("dilate", morp);cv2.waitKey(0);cv2.destroyWindow("dilate")
morp = cv2.GaussianBlur(morp,(13,13),3, 3, borderType=cv2.BORDER_REFLECT_101)
cv2.imshow("GaussianBlur", morp);cv2.waitKey(0);cv2.destroyWindow("GaussianBlur")
morp = cv2.erode(morp, kernel, iterations=3)
cv2.imshow("erode", morp);cv2.waitKey(0);cv2.destroyWindow("erode")

# circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=35, minRadius=80, maxRadius=120)
circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=35, minRadius=75, maxRadius=120 )

for i in circles[0]:
    cv2.circle(dst, ((int)(i[0]), (int)(i[1])), (int)(i[2]), (255, 255, 255), 5)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()