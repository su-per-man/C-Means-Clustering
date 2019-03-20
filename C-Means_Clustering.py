import pandas as pd
import random
from statistics import mean
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math

def readFile():
    df=pd.read_csv('iris.csv')
    for index,row in df.iterrows():
        dataset.append([row['sepal_length']])
        dataset[index].append(row['sepal_width'])
        dataset[index].append(row['petal_length'])
        dataset[index].append(row['petal_width'])
    return

##Program starts here --
dataset=[]
readFile()
print("Total no. of data : ",len(dataset))
clusterHeads=random.sample(dataset,3)
print("INITIAL CLUSTER HEADS : ",*clusterHeads,sep="\n")
for itr in range(0,200):
    cluster=[[],[],[]]
    for i in range(len(dataset)):
        x,y,z,w=dataset[i][0],dataset[i][1],dataset[i][2],dataset[i][3]
        d=[]
        for j in range(0,3):
            d.append(math.sqrt((clusterHeads[j][0] - x)**2 + (clusterHeads[j][1] - y)**2 + (clusterHeads[j][2] - z)**2 + (clusterHeads[j][3] - w)**2))
        if d[0]<d[1] and d[0]<d[2]:
            cluster[0].append(dataset[i])
        elif d[2]<d[1]:
            cluster[2].append(dataset[i])
        else:
            cluster[1].append(dataset[i])
    clusterHeads=[[],[],[]]
    ## calculating mean
    for cl in range(0,3):
        X,Y,Z,W=[],[],[],[]
        for i in range(len(cluster[cl])):
            X.append(cluster[cl][i][0])
            Y.append(cluster[cl][i][1])
            Z.append(cluster[cl][i][2])
            W.append(cluster[cl][i][3])
        X=mean(X)
        Y=mean(Y)
        Z=mean(Z)
        W=mean(W)
        clusterHeads[cl].append(round(X,3))
        clusterHeads[cl].append(round(Y,3))
        clusterHeads[cl].append(round(Z,3))
        clusterHeads[cl].append(round(W,3))
    print("ITERATION : ",itr,*clusterHeads,sep="\n")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')        
for cl in range(0,3):
    X,Y,Z,W=[],[],[],[]
    for i in range(len(cluster[cl])):
        X.append(cluster[cl][i][0])
        Y.append(cluster[cl][i][1])
        Z.append(cluster[cl][i][2])
        W.append(cluster[cl][i][3])
    col=['red','blue','yellow']
    ax.scatter([clusterHeads[cl][0]],[clusterHeads[cl][1]],[clusterHeads[cl][2]],[clusterHeads[cl][3]], c='black',s=30, cmap=plt.hot())
    ax.scatter(X, Y, Z,W, c=col[cl], cmap=plt.hot(),alpha=0.5)
    #ax.legend()
plt.show()
