import cv2

image1 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_UNCHANGED)
image2 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_COLOR)
image4 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_ANYDEPTH)
image5 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_ANYCOLOR)
image6 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_2)
image7 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4)
image8 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_8)
image9 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_REDUCED_COLOR_2)
image10 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_REDUCED_COLOR_4)
image11 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_REDUCED_COLOR_8)
image12 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_LOAD_GDAL)
image13 = cv2.imread("Image/S1000rr.jpg", cv2.IMREAD_IGNORE_ORIENTATION)

cv2.imshow("IMREAD_UNCHANGED",image1)
cv2.imshow("IMREAD_GRAYSCALE",image2)
cv2.imshow("IMREAD_COLOR",image3)
cv2.imshow("IMREAD_ANYDEPTH",image4)
cv2.imshow("IMREAD_ANYCOLOR",image5)
cv2.imshow("IMREAD_REDUCED_GRAYSCALE_2",image6)
cv2.imshow("IMREAD_REDUCED_GRAYSCALE_4",image7)
cv2.imshow("IMREAD_REDUCED_GRAYSCALE_8",image8)
cv2.imshow("IMREAD_REDUCED_COLOR_2",image9)
cv2.imshow("IMREAD_REDUCED_COLOR_4",image10)
cv2.imshow("IMREAD_REDUCED_COLOR_8",image11)
cv2.imshow("IMREAD_LOAD_GDAL",image12)
cv2.imshow("IMREAD_IGNORE_ORIENTATION",image13)

cv2.waitKey()
cv2.destroyAllWindows()

"""
cv2.IMREAD_UNCHANGED : 원본 사용
cv2.IMREAD_GRAYSCALE : 1 채널, 그레이스케일 적용
cv2.IMREAD_COLOR : 3 채널, BGR 이미지 사용
cv2.IMREAD_ANYDEPTH : 이미지에 따라 정밀도를 16/32비트 또는 8비트로 사용
cv2.IMREAD_ANYCOLOR : 가능한 3 채널, 색상 이미지로 사용
cv2.IMREAD_REDUCED_GRAYSCALE_2 : 1 채널, 1/2 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_4 : 1 채널, 1/4 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_GRAYSCALE_8 : 1 채널, 1/8 크기, 그레이스케일 적용
cv2.IMREAD_REDUCED_COLOR_2 : 3 채널, 1/2 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_4 : 3 채널, 1/4 크기, BGR 이미지 사용
cv2.IMREAD_REDUCED_COLOR_8 : 3 채널, 1/8 크기, BGR 이미지 사용
cv2.IMREAD_LOAD_GDAL : 이미지를 GDAL드라이버를 활용하여 읽는다.(GDAL : 지도관련 이미지 처리)
cv2.IMREAD_IGNORE_ORIENTATION : EXIF flag 에 따라 이미지 회전하지 않음
height, width , channel = image.shape를 이용하여 해당 이미지의 높이, 너비, 채널의 값을 확인할 수 있습니다.
"""