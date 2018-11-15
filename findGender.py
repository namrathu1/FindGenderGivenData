# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:08:14 2018

@author: SmithaK
"""

from sklearn import tree

# height weight shoe size
X = [[180,80,44],[170,70,43],[160,60,38],
     [154,54,37],[166,65,40],[190,90,47],
     [175,64,39],[177,70,40],[171,75,42],
     [181,85,43]]

Y = ['male','female','female',
     'female','female','male',
     'male','male','male',
     'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction  = clf.predict([[180,84,44]])

print(prediction)
