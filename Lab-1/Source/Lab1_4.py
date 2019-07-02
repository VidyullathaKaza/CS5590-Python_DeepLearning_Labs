import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Car_sales.csv')

dataset.Price_in_thousands.describe()
dataset.info()
#Working with Numeric Features
numeric_features = dataset.select_dtypes(include=[np.number])

corr = numeric_features.corr()

print (corr['Price_in_thousands'].sort_values(ascending=False)[:5], '\n')

##Null values
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False)[:12])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)


##handling missing value
data = dataset.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

# Drop any nan values if any exist
data_frame = data.select_dtypes(include=[np.number]).interpolate().dropna()

# If the column is non-numeric, dummify the data
for column in data_frame:
    if np.issubdtype(data_frame[column].dtype, np.number) == False:
        data_frame = pd.get_dummies(
            data_frame,
            columns=[column]
        )

##Build a linear model
y = np.log(data_frame.Price_in_thousands)
X = data_frame.drop(['Sales_in_thousands', 'Horsepower', 'Price_in_thousands', 'Engine_size', 'Wheelbase', 'Width', 'Length', 'Curb_weight','Fuel_capacity','Fuel_efficiency'], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)


##Evaluate the performance and visualize results
print("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print('RMSE is: \n', mean_squared_error(y_test, predictions))