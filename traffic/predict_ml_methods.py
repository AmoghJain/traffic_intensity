import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor 
import sys
from datetime import datetime

weekday = datetime.today().weekday()
now = datetime.now()

hour = now.hour
minute = now.minute

data = pd.read_csv("intensity_data_sushmitha.tsv", delimiter="\t")

X = data[['day_of_week', 'hour', 'minute']]
X = np.array(X)
Y = np.array(data['intensity'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=4)

ad = AdaBoostRegressor().fit(X_train, y_train)
#print(np.average(np.abs(ad.predict(X_test) - y_test)))

gb = GradientBoostingRegressor().fit(X_train, y_train)
#print(np.average(np.abs(gb.predict(X_test) - y_test)))

print("The current traffic intensity predictions at Silkboard junction")
print("According to AdaBoostRegressor algorithm : ", ad.predict([[weekday, hour, minute]])[0])
print("According to GradientBoostingRegressor algorithm : ", gb.predict([[weekday, hour, minute]])[0])

print("\n")

data = pd.read_csv("intensity_data_thilak.tsv", delimiter="\t")

X = data[['day_of_week', 'hour', 'minute']]
X = np.array(X)
Y = np.array(data['intensity'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=4)

ad = AdaBoostRegressor().fit(X_train, y_train)
#print(np.average(np.abs(ad.predict(X_test) - y_test)))

gb = GradientBoostingRegressor().fit(X_train, y_train)
#print(np.average(np.abs(gb.predict(X_test) - y_test)))

print("The current traffic intensity predictions at Hebbal flyover ")
print("According to AdaBoostRegressor algorithm : ", ad.predict([[weekday, hour, minute]])[0])
print("According to GradientBoostingRegressor algorithm : ", gb.predict([[weekday, hour, minute]])[0])