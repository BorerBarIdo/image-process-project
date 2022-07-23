import cv2 as cv2


def comparisonSample(sample, img):
	method = cv2.TM_CCOEFF
	ret2, sample_tresh = cv2.threshold(sample, 127, 255, cv2.THRESH_BINARY)
	# ret2, img_tresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
	result = cv2.matchTemplate(img, sample_tresh, method)
	mn, _, mnLoc, _ = cv2.minMaxLoc(result)
	return mn, mnLoc
