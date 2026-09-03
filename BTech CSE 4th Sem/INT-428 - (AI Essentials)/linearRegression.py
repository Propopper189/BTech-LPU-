from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np

X, y = fetch_california_housing(return_X_y=True, as_frame=True)

#Select single feature
x_single = X[['AveRooms']]
x_train_s, x_test_s, y_train_s, y_test_s = train_test_split(x_single, y, test_size=0.2, random_state=42)

#Model
lr = LinearRegression()
lr.fit(x_train_s, y_train_s)

#Prediction
y_pred_s = lr.predict(x_test_s)

#Evaluation
mse_s = mean_squared_error(y_test_s, y_pred_s)
print("Linear Regression (Single Feature) MSE:", mse_s)

#Coefficient
print("Coefficient: ", lr.coef_)
print("Intercept:", lr.intercept_)