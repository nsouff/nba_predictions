import sklearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import os

graph_dir = "graphs"
if not os.path.exists(graph_dir):
    os.mkdir(graph_dir)


data = pd.read_csv('historical_data.csv')
used_data = ['G', 'MP', 'PTS', 'TRB', 'AST', 'STL', 'BLK', 'FG%', 'FT%', 'win_perc']
predict = 'Share'
X = np.array(data[used_data])
Y = np.array(data[predict])

model = LinearRegression()
model.fit(X, Y)
actual = pd.read_csv('current_data.csv')
names = actual['Player']
actual = np.array(actual[used_data])
predictions = model.predict(actual)
shares = list(zip(names, predictions))
shares.sort(key=lambda x: x[1])
shares = shares[-10:]
shares.reverse()
names = []
votes = []
for tup in shares:
    names.append(tup[0])
    votes.append(tup[1])
coef = list(zip(used_data, model.coef_))
style.use('seaborn')
fig, ax = plt.subplots()
ax.bar(np.arange(len(votes)), votes, width=0.7, linewidth=1, color='gold')
rects = ax.patches
for rect, label in zip(rects, names):
    height = .03
    ax.text(rect.get_x() + rect.get_width() / 1.75, height, label,
    ha='center', va='bottom', rotation = 'vertical', color = 'black')

ax.xaxis.set_visible(False)
ax.set_title("2020 MVP prediction",fontsize=20)
ax.set_ylabel("Predicted votes shares")

plt.savefig(os.path.join(graph_dir,'result.png'))
plt.close()
for i in used_data:
    fig, ax = plt.subplots()
    plt.scatter(data[i], data[predict])
    plt.xlabel(i)
    plt.ylabel("Vote shares")
    plt.savefig(os.path.join(graph_dir, i + ".png"))
    plt.close()
