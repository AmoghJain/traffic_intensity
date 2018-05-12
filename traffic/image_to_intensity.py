import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

def get_intensities(image):

	img = cv2.imread(image)
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	high = 0
	mid = 0
	low = 0

	for row_i in range(len(hsv_img)):
		for pixel_i in range(len(hsv_img[row_i])):
			if 1 <= hsv_img[row_i][pixel_i][0] < 10 or (img[row_i][pixel_i][2] > 80 and img[row_i][pixel_i][1] < 60):
				high += 1
			elif img[row_i][pixel_i][2] < 135 and img[row_i][pixel_i][1] > 200:
				mid += 1
			elif img[row_i][pixel_i][2] == 255 and img[row_i][pixel_i][1] == 151 and img[row_i][pixel_i][0] == 77:
				low += 1

	try:			
		total = high+low+mid

		upper_limit = total * 3
		actual_intensity = high*3 + mid*2 + low
		congestion_ratio = 1.0*actual_intensity/upper_limit
		
		return congestion_ratio
	except:
		return None

# get_intensities(sys.argv[1])