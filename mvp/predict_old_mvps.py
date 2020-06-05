import sklearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
from operator import itemgetter

# Predicts old MVPs
data = pd.read_csv('historical_data.csv')
used_data = ['G', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', 'FT%', 'win_perc']
predict = 'Share'


good_pick = 0
for i in range(1979, 2019):
    year_data = data[data.season_start == i]
    names = year_data["Player"]
    other_year_data = data[data.season_start != i]
    X = np.array(other_year_data[used_data])
    Y = np.array(other_year_data[predict])
    model = LinearRegression()
    model.fit(X, Y)
    predictions = model.predict(np.array(year_data[used_data]))
    predictions = list(zip(names, predictions))
    predictions.sort(key=itemgetter(1))
    predictions.reverse()
    mvp = year_data[year_data.Rank == 1]
    if mvp.iloc[0]['Player'] == predictions[0][0]:
        good_pick+=1
    else:
        print("in", i, mvp.iloc[0]['Player'],"would not be but", predictions[0][0], "would be")
print(good_pick)
