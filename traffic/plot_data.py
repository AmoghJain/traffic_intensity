import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

data_file = sys.argv[1]

plot_data = open(data_file).readlines()

X = plot_data[0]
X = [float(x) for x in X.split("\t")]
Y1 = plot_data[1]
Y1 = [float(y) for y in Y1.split("\t")]
Y2 = plot_data[2]
Y2 = [float(y) for y in Y2.split("\t")]
Y3 = plot_data[3]
Y3 = [float(y) for y in Y3.split("\t")]
Y4 = plot_data[4]
Y4 = [float(y) for y in Y4.split("\t")]
Y5 = plot_data[5]
Y5 = [float(y) for y in Y5.split("\t")]
Y6 = plot_data[6]
Y6 = [float(y) for y in Y6.split("\t")]
Y7 = plot_data[7]
Y7 = [float(y) for y in Y7.split("\t")]

f = plt.figure(figsize=(20,20))

plt.subplot(421)
plt.plot(X, Y1)
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Monday")
plt.grid(True)

plt.subplot(422)
plt.plot(X, Y2, "r")
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Tuesday")
plt.grid(True)

plt.subplot(423)
plt.plot(X, Y3, "y")
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Wednseday")
plt.grid(True)

plt.subplot(424)
plt.plot(X, Y4, "g")
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Thursday")
plt.grid(True)

plt.subplot(425)
plt.plot(X, Y5, "k")
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Friday")
plt.grid(True)

plt.subplot(426)
plt.plot(X, Y6, "c")
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Saturday")
plt.grid(True)

plt.subplot(427)
plt.plot(X, Y7, "m")
plt.xlabel('Time')
plt.ylabel('Intensity')
plt.title("Sunday")
plt.grid(True)

plt.subplot(428)
plt.plot(X, Y1, X, Y2,"r", X, Y3, "y", X, Y4, "g", X, Y5, "k", X, Y6, "c", X, Y7, "m")
plt.grid(True)

plt.tick_params(axis='both', which='major', labelsize=10)
# f.savefig("day_of_week_intensities_hebbal.png")

days_intensities = plot_data[1:]

avg_intensities = []
for day_intensities in days_intensities:
    avg_intensity = np.average([float(day_intensity) for day_intensity  in day_intensities.split("\t")])
    avg_intensities.append(avg_intensity)
    
f = plt.figure(figsize=(12,9))
y_pos = np.arange(len(avg_intensities))

plt.bar(y_pos, avg_intensities, align='center', alpha=0.5)
plt.xticks(y_pos, ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])
plt.yticks(np.arange(0.0, 0.8, step=0.05))
plt.ylabel('Traffic congestions')
plt.xlabel("Day")
plt.title('Daywise congestions')
# f.savefig("day_wise_intensities_hebbal.png")
plt.show()

plot_data = pd.read_csv(data_file, delimiter="\t")

time_points = []
avg_intensities = []

for col in plot_data.columns: 
    avgs = np.average(plot_data[col])
    time_points.append(col)
    avg_intensities.append(avgs)

f = plt.figure(figsize=(20,8))
y_pos = np.arange(len(avg_intensities))
plt.bar(y_pos, avg_intensities, align='center', alpha=0.5)
plt.xticks(y_pos, time_points, rotation=45)
plt.ylabel('Traffic congestions')
plt.xlabel("Time")
# f.savefig("hour_wise_intensities_hebbal.png")
plt.show()
