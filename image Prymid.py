import cv2

src = cv2.imread("F:\dev\opencv\image\cat.jpg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)

cv2.waitKey()
cv2.destroyAllWindows()


"""
픽셀 외삽법 종류

속성	의미
cv2.BORDER_CONSTANT	    iiiiii | abcdefgh | iiiiiii
cv2.BORDER_REPLICATE	aaaaaa | abcdefgh | hhhhhhh
cv2.BORDER_REFLECT	    fedcba | abcdefgh | hgfedcb
cv2.BORDER_WRAP	        cdefgh | abcdefgh | abcdefg
cv2.BORDER_REFLECT_101	gfedcb | abcdefgh | gfedcba
cv2.BORDER_REFLECT101	gfedcb | abcdefgh | gfedcba
cv2.BORDER_DEFAULT	    gfedcb | abcdefgh | gfedcba
cv2.BORDER_TRANSPARENT	uvwxyz | abcdefgh | ijklmno
cv2.BORDER_ISOLATED	    관심 영역 (ROI) 밖은 고려하지 않음



이미지 확대 함수는 BORDER_DEFAULT의 픽셀 외삽법만 사용할 수 있습니다.

이미지 축소 함수는 BORDER_CONSTANT의 픽셀 외삽법을 제외한 나머지 플래그만 사용할 수 있습니다.

"""