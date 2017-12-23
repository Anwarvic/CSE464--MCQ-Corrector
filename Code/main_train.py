import pandas as pd
import cv2

# ------- Importing Code Files -------
from show import show_image
from grading import grade_all
from map import image_transform


df = pd.read_csv('train.csv', usecols=['FileName', 'Mark'])

image_list = df['FileName']
total_marks = df['Mark']

grade = []
match = []
mapped = []

for i in range(len(image_list)):
	print image_list[i]
	warped = image_transform('train/'+ image_list[i])
	grade.append(grade_all(warped)) 
	if grade[i] == total_marks[i]:
		match.append(True)
	else:
		match.append(False)


df['Grade'] = grade
df['Match'] = match
df.to_csv('train4_7.csv')


# mapped = []
# for i in range(len(image_list)):
# 	print image_list[i]
# 	warped = image_transform('train/'+ image_list[i])
# 	if warped is None:
# 		mapped.append(False)
# 	else:
# 		mapped.append(True)


# df['Mapped'] = mapped
# df.to_csv('train3_7.csv')
	
			
    

#print grade_all(warped)