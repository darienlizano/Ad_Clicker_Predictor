#importing packages
import pandas as pd
import numpy as np

#loading data
ad_data = pd.read_csv('advertising.csv')

#dropping cols we dont need before data split
ad_data.drop(['Ad Topic Line','City','Country','Timestamp'],axis=1,inplace=True)

#creating X and y arrays for split
X=ad_data.drop('Clicked on Ad',axis=1)
y=ad_data['Clicked on Ad']

#importing package for split
from sklearn.model_selection import train_test_split

#spliting data with test size od 30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#loading paackage for logistic regression
from sklearn.linear_model import LogisticRegression

#creating model
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

#loading package for classification report
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))