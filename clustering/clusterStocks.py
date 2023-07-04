import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from config import mydb

###The big decision is whether to cluster on a single day or the whole stock history
#Get the data from MongoDBa
tickersReturns = {}
for collection in mydb.list_collection_names():
    tickerColl = mydb[collection]
    query = {"$and":[
                {"open":{"$gt":0}},
                {"datetime":{"$regex":"2023-05-02"}}
    ]}
    results = list(tickerColl.find(query))
    #print(collection)
    #print(results)
    #Create a numpy array of the open/close prices
    openPrices = np.array([candle['open'] for candle in results])
    closePrices = np.array([candle['close'] for candle in results])
    #Reshape the array to be a 2D array
    openPrices = openPrices.reshape(-1,1)
    closePrices = closePrices.reshape(-1,1)
    #Create a numpy array of the days' returns
    daysReturn = [(close-open) / open for open,close in zip(openPrices,closePrices)]

    try:
        tickersReturns[collection] = daysReturn[-1]
    except:
        continue

#Create a kmeans model
kmeans = KMeans(n_clusters=3)
#Fit the model to the data
kmeans.fit(list(tickersReturns.values()))
labels = kmeans.labels_
centers = kmeans.cluster_centers_

#Visualize the clusters
plt.scatter(list(tickersReturns.values()),np.zeros(len(tickersReturns.values())),c=labels)
plt.scatter(centers,np.zeros(len(centers)),c='red')
plt.title('Clusters of Stocks')
plt.xlabel('Returns')
plt.show()

#    print(daysReturn)