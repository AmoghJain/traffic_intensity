import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor 
import sys

data = pd.read_csv(sys.argv[1], delimiter="\t")

X = data[['day_of_week', 'hour', 'minute']]
X = np.array(X)
Y = np.array(data['intensity'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=4)

ad = AdaBoostRegressor().fit(X_train, y_train)
#print(np.average(np.abs(ad.predict(X_test) - y_test)))

gb = GradientBoostingRegressor().fit(X_train, y_train)
#print(np.average(np.abs(gb.predict(X_test) - y_test)))

print(ad.predict([[0, 8, 15]]))
print(gb.predict([[0, 8, 15]]))