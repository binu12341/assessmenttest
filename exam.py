# -*- coding: utf-8 -*-
"""Exam.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y6cQhgSuIyYX-Q-g2saf1oLab575ANhy
"""

import pandas as pd
import numpy as np

data = pd.read_csv("/content/train_v9rqX0R.csv")

data

data.head()

data.tail()

data.describe()

data.columns

data.shape

data.isna().sum()

data=data.drop(["Item_Weight","Outlet_Size"],axis=1)

data.isna().sum()

data.dtypes

from matplotlib import pyplot as plt

data['Item_Visibility'].plot(kind="box")
plt.show()

data['Item_Visibility'].describe().round()

data['Item_MRP'].plot(kind="box")
plt.show()

data['Item_MRP'].describe().round()

data['Outlet_Establishment_Year'].plot(kind="box")
plt.show()

data['Outlet_Establishment_Year'].describe().round()

data['Item_Outlet_Sales'].plot(kind="box")
plt.show()

data['Item_Outlet_Sales'].describe().round()

data['Item_Identifier'].value_counts()

data.columns

req_cols=['Item_Identifier', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
       'Item_MRP', 'Outlet_Identifier', 'Outlet_Establishment_Year',
       'Outlet_Location_Type', 'Outlet_Type']

x = data[req_cols]

y=data['Outlet_Establishment_Year']

y.value_counts(normalize = True) * 100

x.columns

x.shape

x = pd.get_dummies(x)

x.info()

x.describe()

from sklearn.preprocessing import MinMaxScaler

y.value_counts()

from sklearn.model_selection import train_test_split

x_train, x_test , y_train, y_test = train_test_split(x,y, test_size = 0.2)

sc = MinMaxScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

from sklearn.linear_model import LogisticRegression

lg = LogisticRegression(max_iter = 5000)

lg.fit(x_train, y_train)

y_pred = lg.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix

acc = accuracy_score(y_test, y_pred)

acc

confusion_matrix(y_test, y_pred)

y_test.value_counts()

from sklearn.ensemble import GradientBoostingRegressor

Final_model = GradientBoostingRegressor(learning_rate=0.16, max_depth=3, n_estimators=35)
Final_model.fit(x_train, y_train)

final_predictions = Final_model.predict(x_test)

df_sol = pd.read_csv('sample_submission_8RXa3c6.csv')
df_sol.head()

df_submission = df_sol.copy()

final_predictions = Final_model.predict(x_test)

df_submission.to_csv('final_submission.csv', index=False)