import sklearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle


data = pd.read_csv('historical_data.csv')
used_data = ['G', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', '3P%', 'FT%', 'win_perc']
predict = 'Share'
X = np.array(data[used_data])
Y = np.array(data[predict])

model = LinearRegression()
model.fit(X, Y)
actual = pd.read_csv('current_data.csv')
names = actual['Player']
actual = np.array(actual[used_data])
predictions = model.predict(actual)
for i in range(len(predictions)):
    if predictions[i] > 0.2:
        print(names[i], predictions[i])
