import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def extract_traffic_layer(base_dir):

	output_parent_directory = base_dir[:-1]+"_processed/"
	if not os.path.exists(output_parent_directory):
		os.makedirs(output_parent_directory)

	for dir_ in os.listdir(base_dir):
		output_directory = output_parent_directory+dir_
		if not os.path.exists(output_directory):
			os.makedirs(output_directory)

		dir_ = dir_ + "/"
		output_directory += "/"

		for file_ in os.listdir(base_dir+dir_):
			print(base_dir+dir_+file_)
			img = cv2.imread(base_dir+dir_+file_)
			hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

			processed_img = []

			for row_i in range(len(hsv_img)):
				new_row = []
				for pixel_i in range(len(hsv_img[row_i])):
					if 1 <= hsv_img[row_i][pixel_i][0] < 10 or (img[row_i][pixel_i][2] > 80 and img[row_i][pixel_i][1] < 60):
						new_row.append(img[row_i][pixel_i])
					elif img[row_i][pixel_i][2] < 135 and img[row_i][pixel_i][1] > 200:
						new_row.append(img[row_i][pixel_i])
					elif img[row_i][pixel_i][2] == 255 and img[row_i][pixel_i][1] == 151 and img[row_i][pixel_i][0] == 77:
						new_row.append(img[row_i][pixel_i])
					else:
						new_row.append(np.zeros(3))
				processed_img.append(new_row)

			processed_img = np.asarray(processed_img)
			cv2.imwrite(output_directory+file_, processed_img)
			# break

extract_traffic_layer(sys.argv[1])

# total = high+mid+low

# upper_limit = total*3
# actual_intensity = high*3 + mid*2 + low*1

# congestion_ratio = 1.0*actual_intensity/upper_limit

# print "congestion ratio is ", congestion_ratio
