import numpy as np
import cv2
import heapq


from crop import crop_image
from show import show_image

from map import image_transform

debug = 0

FINAL_ANSWER_1 = [1, 2, 0, 0, 3, 0, 2, 2, 0, 2, 0, 1, 2, 2, 1]
FINAL_ANSWER_2 = [0, 3, 1, 2, 1, 3, 2, 3, 1, 3, 2, 3, 3, 1, 2]
FINAL_ANSWER_3 = [1, 1, 3, 2, 1, 2, 1, 2, 2, 0, 1, 1, 2, 2, 1]


def get_questions(image_part):
	q = []
	rows, cols = image_part.shape
	for i in range(15):
		start = i*rows/15
		end = (i+1) * rows/15
		question = image_part[start:end]
		q.append(question)
	return q

def grade_question(choices_list, final_answer):
	means_list = []
	first_choice, second_choice, third_choice, fourth_choice = choices_list
	temp = 0
	means_list.append(cv2.countNonZero(first_choice))
	means_list.append(cv2.countNonZero(second_choice))
	means_list.append(cv2.countNonZero(third_choice))
	means_list.append(cv2.countNonZero(fourth_choice))
	if debug:
		print means_list, final_answer #------------------------------------------------------------------------------------------
	
	max1, max2 = heapq.nlargest(2, means_list)

	if max1 > 250 and max2 > 250:		#two answers
		return 0
	elif max1 > 250 and max2 > 200 and max2 < 250:		#eraser case
		temp += 1
	elif max1 > 200 and max2 < 200:		#light pencil
		temp += 1
	else:								#no answers
		return 0

	if temp == 1 and means_list.index(max1) == final_answer:
		return 1
	else:
		return 0

def get_choices_1(row):
	first_choice = 	row[:,100:140]
	second_choice = row[:,140:180]
	third_choice = row[:,180:220]
	fourth_choice = row[:,220:260]

	return first_choice, second_choice, third_choice, fourth_choice



def get_choices_2(row):
	first_choice = 	row[:,115:155]
	second_choice = row[:,155:195]
	third_choice = row[:,195:235]
	fourth_choice = row[:,235:275]

	return first_choice, second_choice, third_choice, fourth_choice

def get_choices_3(row):
	first_choice = 	row[:,135:175]
	second_choice = row[:,175:215]
	third_choice = row[:,215:255]
	fourth_choice = row[:,255:295]

	return first_choice, second_choice, third_choice, fourth_choice


def grade_1(image_part):
	correct = 0
	questions = get_questions(image_part)
	for i in range(15):
		if debug:
			show_image(questions[i]) #------------------------------------------------------------------------------------------
		choices_list = get_choices_1(questions[i])
		correct += grade_question(choices_list, FINAL_ANSWER_1[i])
		if debug:
			print correct #------------------------------------------------------------------------------------------
	return correct


def grade_2(image_part):
	correct = 0
	questions = get_questions(image_part)
	for i in range(15):
		if debug:
			show_image(questions[i]) #------------------------------------------------------------------------------------------
		choices_list = get_choices_2(questions[i])
		correct += grade_question(choices_list, FINAL_ANSWER_2[i])
		if debug:
			print correct #------------------------------------------------------------------------------------------
	return correct

def grade_3(image_part):
	correct = 0
	questions = get_questions(image_part)
	for i in range(15):
		if debug:
			show_image(questions[i]) #------------------------------------------------------------------------------------------
		choices_list = get_choices_3(questions[i])
		correct += grade_question(choices_list, FINAL_ANSWER_3[i])
		if debug:
			print correct #------------------------------------------------------------------------------------------
	return correct


def grade_all(warped):
	total_grade = 0
	
	try:
		gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
		thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	except:
		thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

	if debug:
		show_image(thresh) #------------------------------------------------------------------------------------------
	first_part, second_part, third_part = crop_image(thresh)
	total_grade = grade_1(first_part) + grade_2(second_part) + grade_3(third_part)
	
	return total_grade



#------------------------------------------------------------------------------------------
# warped = image_transform("train/"+"S_8_hppscan138.png")
# if debug:
# 	show_image(warped)
# print grade_all(warped)








