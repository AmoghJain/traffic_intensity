import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("scr3.png")
high = 0
mid = 0
low = 0

new_image = []
for row in img:
	new_row = []
	for col in row:
		if col[2] > 120 and col[1] < 50: # red
			# high+=1
			new_row.append(col)
		elif col[2] < 135 and col[1] > 200: # green 
			# low+=1
			new_row.append(col)
		elif col[2] > 200 and col[1] > 100 and col[0] < 20: # orange
			# mid+=1
			new_row.append(col)
		else:
			new_row.append(np.array([0,0,0]))
	new_image.append(new_row)

new_image = np.array(new_image)
cv2.imwrite("processed3.png", new_image)

# total = high+mid+low

# upper_limit = total*3
# actual_intensity = high*3 + mid*2 + low*1

# congestion_ratio = 1.0*actual_intensity/upper_limit

# print "congestion ratio is ", congestion_ratio
