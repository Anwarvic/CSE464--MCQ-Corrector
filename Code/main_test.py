import pandas as pd
import cv2

# ------- Importing Code Files -------
from show import show_image
from grading import grade_all
from map import image_transform


df = pd.read_csv('test.csv', usecols=['FileName'])
image_list = df['FileName']

grade = []

for i in range(len(image_list)):
	print image_list[i]
	warped = image_transform('test/'+ image_list[i])
	grade.append(grade_all(warped)) 


df['Grade'] = grade
df.to_csv('test_3.csv')
