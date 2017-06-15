import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
style.use('ggplot')
df=pd.read_csv("C:\\Users\\Biswas\\Desktop\\sample.csv")
print(df)
df.values
print(df.values)

X = np.array(df.values)


plt.scatter(X[:, 0],X[:, 1], s=150, linewidths = 5, zorder = 10)
#plt.show()


clf = KMeans(n_clusters=3)
clf.fit(X)
centroids = clf.cluster_centers_
labels = clf.labels_
colors = ["g.","r.","c.","y."]
for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()