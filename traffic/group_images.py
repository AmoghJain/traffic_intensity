import os
import time
import sys
# from image_to_intensity import get_intensities
# import cv2
from shutil import copy2

images = os.listdir(sys.argv[1])

master_list = []

continous_list = []
for i in range(len(images)-1):
	try:
		image_1 = ".".join(images[i][:-4].split("_"))
		image_2 = ".".join(images[i+1][:-4].split("_"))
		minutes_diff = (float(image_2) - float(image_1))/60.0
		if minutes_diff < 20:
			if image_1 not in continous_list:
				continous_list.append(image_1)
			continous_list.append(image_2)
		else:
			master_list.append(continous_list)
			continous_list = []
			continous_list.append(image_2)
	except Exception as e:
		pass

count = 0
for l in master_list:
	des_folder_path = "".join([sys.argv[1],"grouped/",str(count),"/"])
	if not os.path.exists(des_folder_path):
		os.makedirs(des_folder_path)
	for image in l:
		src_img_path = "".join([sys.argv[1],"_".join(image.split("."))+".png"])
		print(src_img_path)
		des_img_path = des_folder_path+"_".join(image.split("."))+".png"
		copy2(src_img_path, des_img_path)
	count += 1		