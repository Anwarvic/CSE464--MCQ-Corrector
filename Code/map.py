import cv2
from imutils.perspective import four_point_transform
import numpy as np
from show import show_image
 

DEBUG = 0


def image_trans(image):
	if DEBUG:
		show_image(image)
	
	edged = cv2.Canny(image, 75, 200)
	if DEBUG:
		show_image(edged)

	thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	hybrid = edged + thresh
	hybrid = edged + thresh
	
	if CASE == 0:
		img, cnts, hierarchy = cv2.findContours(hybrid.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)	
	elif CASE == 1:
		img, cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	
	docCnt = None 
	if len(cnts) > 0:
		cnts = sorted(cnts, key=cv2.contourArea, reverse=True)	 
		for c in cnts:
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.01 * peri, True)

			if len(approx) == 4:
				docCnt = approx
				break

	if docCnt is None:
		if DEBUG:
			print "No contour is found"
		return None, None

	warped = four_point_transform(IMAGE, docCnt.reshape(4, 2))
	if DEBUG:
		cv2.drawContours(image, [docCnt], -1, 255, -1)
		show_image(image)
	return warped, cv2.contourArea(docCnt)


def increase_contrast(image_name):
	image = cv2.imread(image_name)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (7, 7), 0)

	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(20,20))
	cl1 = clahe.apply(blurred)
	return cl1



def image_transform(image_name):
	image = cv2.imread(image_name)
	global IMAGE, CASE
	CASE = 0
	IMAGE = image

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (7, 7), 0)
	while(CASE < 2):
		warped, cntArea = image_trans(blurred)
		if cntArea > 1000000:
			return warped[440:, :]
		elif cntArea > 600000:
			return warped
		else:
			image = increase_contrast(image_name)
			rows, cols = image.shape
			warped, cntArea = image_trans(image)
			if cntArea > 600000:
				return warped
		CASE += 1
	
	if DEBUG:
		print "Less than 600,000", cntArea
		return None
	
	return IMAGE[660:rows-250]
	# return None

#------------------------------------------------------------------------------------------
# warped= image_transform('test/'+ "S_1_hppscan111.png")
# if warped is not None:
# 	show_image(warped)
# cv2.imwrite("yarab.png", warped)
