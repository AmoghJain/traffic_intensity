import os
import sys
import datetime

from image_to_intensity import get_intensities

fw = open("intensity_data.tsv", "w")

def create_tsv(base_dir):
	 
	for dir_ in os.listdir(base_dir):
		group_dir = base_dir + dir_

		group_id = dir_

		for image_f in os.listdir(group_dir):
			print(image_f)
			time_stamp = ".".join(image_f.split(".")[0].split("_"))
			
			full_date = datetime.datetime.fromtimestamp(float(time_stamp)).strftime('%Y-%m-%d %H:%M:%S')

			month = full_date.split(" ")[0].split("-")[1]
			day = full_date.split(" ")[0].split("-")[2]
			hour = full_date.split(" ")[1].split(":")[0]
			minutes = full_date.split(" ")[1].split(":")[1]

			day_of_week = datetime.datetime.fromtimestamp(float(time_stamp)).weekday()

			intensity = get_intensities(group_dir+"/"+image_f)

			if intensity:
				fw.write(str(intensity)+"\t"+str(day_of_week)+"\t"+str(month)+"\t"+str(day)+"\t"+str(hour)+"\t"+str(minutes)+"\n")

create_tsv(sys.argv[1])