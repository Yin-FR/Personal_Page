#!/usr/bin/env python3
# -*-coding: utf-8-*-
# @File: titanic_ML.py
# @Author: 檀寅
# @Time: 2020年08月26日11:15
# @说明: 

import pandas as pd
import numpy as np
import json
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def changeEmbarked(x):
    if x == 'S':
        return 0
    elif x == 'C':
        return 1
    else:
        return 2

def changeAge(x):
    if np.isnan(x):
        return 30
    else:
        return x

dataset = pd.read_csv("modules/ML/datasets/titanic/train.csv")
dataset['Sex'] = dataset['Sex'].map(lambda x: 1 if x == 'male' else 0)
dataset['Embarked'] = dataset['Embarked'].map(lambda x: changeEmbarked(x))
dataset['Age'] = dataset['Age'].map(lambda x: changeAge(x))

def titanic_use_model(itemSelected, modelName):
    itemSelected = json.loads(itemSelected)
    items = {}
    for eachItem in itemSelected:
        items[eachItem] = dataset[eachItem]
    X = np.asarray(pd.DataFrame(items))
    y = np.asarray(dataset['Survived'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    if modelName == 'logistic regression':
        clf = LogisticRegression()

    if modelName == 'decision tree':
        clf = DecisionTreeClassifier(max_depth=6)

    if modelName == 'random forest':
        clf = RandomForestClassifier(n_estimators=5, max_depth=10)

    

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc_score = accuracy_score(y_pred=y_pred, y_true=y_test)

    return json.dumps(acc_score)

