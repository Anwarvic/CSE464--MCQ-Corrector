


def crop_image(img):
	rows, cols = img.shape

	cropped = img[60:rows-60,:930]

	first_part = cropped[:,0:310]
	second_part = cropped[:,310:620]
	third_part = cropped[:,620:]
	return first_part, second_part, third_part


