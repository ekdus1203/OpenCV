import cv2

src = cv2.imread("../img/colorball.png.")
dst = src.copy()

image = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,100,param1=100,param2=35,minRadius=80,maxRadius=80)

for i in circles[0]:
    cv2.circle(dst,((int)(i[0]),(int(i[1])),(int)(i[2])), )