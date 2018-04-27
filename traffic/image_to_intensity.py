import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def get_intensities(base_dir):

	# output_directory = base_dir[:-1]+"_processed/"
	# if not os.path.exists(output_directory):
	# 	os.makedirs(output_directory)

	for file_ in os.listdir(base_dir):
		print(file_)
		img = cv2.imread(base_dir+file_)
		high = 0
		mid = 0
		low = 0

		new_image = []
		for row in img:
			new_row = []
			for col in row:
				if col[2] > 120 and col[1] < 50: # red
					high+=1
				elif col[2] < 135 and col[1] > 200: # green 
					low+=1
				elif col[2] > 200 and col[1] > 100 and col[0] < 20: # orange
					mid+=1

		total = high+mid+low

		upper_limit = total*3
		actual_intensity = high*3 + mid*2 + low*1

		congestion_ratio = 1.0*actual_intensity/upper_limit
		return congestion_ratio
		# print("congestion ratio is ", congestion_ratio)

# extract_traffic_layer(sys.argv[1])