# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 14:54:33 2021

@author: peace
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn; seaborn.set() 

rand = np.random.RandomState(42)

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]
X = rand.multivariate_normal(mean, cov, 100)

plt.scatter(X[:, 0], X[:, 1])
indices = np.random.choice(X.shape[0], 20, replace=False)

selection = X[indices]

plt.scatter(X[:, 0], X[:, 1], alpha=0.3)
plt.scatter(selection[:, 0], selection[:, 1],
            facecolor='none', s=200);