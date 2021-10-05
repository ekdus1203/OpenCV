import numpy as np
import cv2

src = cv2.imread("../img/card.jpg")
dst = src.copy()
cv2.imshow("src",src); cv2.waitKey(0);cv2.destroyAllWindows("src")
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),())

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3),(-1,-1))

gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
_,binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
morp = cv2.dilate(binary,kernel)
morp = cv2.erode(morp,kernel,iterations=3)
morp = cv2.dilate(morp,kernel,iterations=2)
canny = cv2.Canny(morp,0,0,apertureSize=3,L2gradient=True)

lines = cv2.HoughLines(canny,1,np.pi/180,140, srn=50, stn=10, min_theta=0, max_theta=np.pi/2)

for i in lines:
    rho, theta = i[0][0], i[0][1]
