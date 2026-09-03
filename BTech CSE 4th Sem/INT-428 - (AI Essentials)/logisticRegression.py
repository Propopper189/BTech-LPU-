import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris(as_frame=True)
df = iris.frame
df = df[df['target'] != 2]

x = df.iloc[:,0:4]
y = df['target']

#Split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Model
model = LogisticRegression(max_iter=100)
model.fit(x_train, y_train)

#Predict
y_pred = model.predict(x_test)

#Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))