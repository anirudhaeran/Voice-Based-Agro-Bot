import numpy as np
import pandas as pd   #data manipulation
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

#preprocessing data
df=pd.read_csv('Crop_recommendation.csv') #reading data from database
x=df.drop('label',axis=1)#inplace=true means it will be deleted from the database otherwise temporarily
y=df['label']

#split the data into training and testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,test_size=0.2)

#training the model
model = RandomForestClassifier()
model.fit(x_train,y_train)
#model evaluation
y_prediction = model.predict(x_test)
accuracy = accuracy_score(y_test,y_prediction)
# print(f"Model Accuracy: {accuracy}")

#saving model to a file
joblib.dump(model,'cropmodel.pkl')

#example
# new_data = np.array([[90,42,43,20,82,6,202]])
# prediction = model.predict(new_data)
# print(f"Prediction for new data: {prediction}")