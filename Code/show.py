import cv2

def show_image(image_name, name = "image", small = False):
 	cv2.namedWindow(name, cv2.WINDOW_NORMAL)
	if small:
		cv2.resizeWindow(name, 500, 300)
	cv2.imshow(name,image_name)
	cv2.waitKey(0)
	cv2.destroyAllWindows()