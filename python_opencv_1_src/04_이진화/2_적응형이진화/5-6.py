import cv2 as cv
import sys


img_color = cv.imread("copy.png", cv.IMREAD_COLOR)
if img_color is None:
	print("이미지 파일을 읽을 수 없습니다.")
	sys.exit(1)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)


_,img_binary = cv.threshold(img_gray,127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU);


cv.imshow('Grayscale', img_gray)
cv.imshow('Binary', img_binary)
cv.waitKey(0)
