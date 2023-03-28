%pip install scipy
%pip install scikit-learn
%pip install seaborn

from scipy.stats import mode


import numpy as np
import pandas as pd

from typing import Tuple

def load_csv(path) -> Tuple[np.ndarray, np.ndarray]:
    np.random.seed(42)
    dataset = np.genfromtxt(path,delimiter = ',')
    np.random.shuffle(dataset)
    x,y = dataset[:,:-1],dataset[:,-1]
    return x,y

x,y = load_csv('iris.csv')
x.shape,y.shape

np.mean(x,axis=0),np.var(x,axis=0)

np.nanmean(x,axis=0),np.nanvar(x,axis=0)

x[np.isnan(x)] = 3.5

y = np.delete(y,np.where(x<0.0)[0],axis=0)
y = np.delete(y,np.where(x>10.0)[0],axis=0)
x = np.delete(y,np.where(x<0.0)[0],axis=0)
x = np.delete(y,np.where(x>10.0)[0],axis=0)

x.shape,y.shape

def train_test_split(features:np.ndarray,labels:np.ndarray,test_split_ratio:float)->Tuple[np.ndarray,np.ndarray,np.ndarray,np.ndarray]:
    test_size = int(len(features)*test_split_ratio)
    train_size = len(features)-test_size

    assert len(features) == test_size+train_size, "Size Mismatch"

    x_train,y_train = features[:train_size,:], labels[:train_size]
    x_test,y_test = features[train_size:,:], labels[train_size:]

    return x_train,y_train,x_test,y_test

x_train,y_train,x_test,y_test = train_test_split(x,y,0.2)

def euclidean(points:np.ndarray,element_of_x:np.ndarray)->np.ndarray:
    return np.sqrt(np.sum(points-element_of_x)**2,axis=1)


def predict(x_train:np.ndarray,y_train:np.ndarray,x_test:np.ndarray,y_test:np.ndarray):
    labels_pred = []
    for x_test_element in x_test:
        distances = euclidean(x_train,x_test_element)
        distances = np.arry(sorted(zip(distances,y_train)))

        label_pred = mode(distances[:k,1],keepdims=False).mode
        labels_pred.append(label_pred)

y_preds = predict(x_train,y_train,x_test,3)
y_preds

def accuracy(y_test,y_preds)->float:
    

