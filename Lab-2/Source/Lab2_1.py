# Linear Regression using Abalone dataset to predict Rings Value using Keras

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout,LeakyReLU
from sklearn.model_selection import train_test_split
from keras import metrics
from keras.optimizers import Adam, RMSprop
from keras.callbacks import TensorBoard

# Creating the Dataframe using abalone.csv
abalone_data = pd.read_csv('abalone.csv')

# As per problem description which require as to compute Age , lets first compute the target of problem 'Age'
# and assign it to dataset abalone_data.  Age = Rings + 1.5
abalone_data['Age'] = abalone_data['Rings']+1.5
abalone_data.drop('Rings', axis=1, inplace=True)

# Feature wise statistics using builtin tools
print(abalone_data.columns)
print(abalone_data.head())
print(abalone_data.info())
print(abalone_data.describe())

# Key Insights
# All Feature are numeric except sex
# no Missing value in dataset
# Creating X and y
feature_cols = ['Length', 'Diameter', 'Height', 'Whole_Weight', 'Shucked_Weight', 'Viscera_Weight', 'Shell_Weight']
X = abalone_data[feature_cols]
y = abalone_data['Age']
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3, random_state=0)
print(X_train.head())
print(y_valid.head())
np.random.seed(155)

# Normalization
def norm_stats(df1, df2):
    dfs = df1.append(df2)
    minimum = np.min(dfs)
    maximum = np.max(dfs)
    mu = np.mean(dfs)
    sigma = np.std(dfs)
    return (minimum, maximum, mu, sigma)

def z_score(col, stats):
    m, M, mu, s = stats
    df2 = pd.DataFrame()
    for c in col.columns:
        df2[c] = (col[c]-mu[c])/s[c]
    return df2

stats = norm_stats(X_train, X_valid)
arr_x_train = np.array(z_score(X_train, stats))
arr_y_train = np.array(y_train)
arr_x_valid = np.array(z_score(X_valid, stats))
arr_y_valid = np.array(y_valid)
print('Training shape:', arr_x_train.shape)
print('Validation',arr_y_train.shape)
print('Training samples: ', arr_x_train.shape[0])
print('Validation samples: ', arr_x_valid.shape[0])

# Defining the Model
def model(x_size, y_size):
    t_model = Sequential()
    t_model.add(Dense(100, activation="tanh", input_shape=(x_size,)))
    t_model.add(Dropout(0.1))
    t_model.add(Dense(50, activation="relu"))
    t_model.add(Dense(20, activation="relu"))
    t_model.add(Dense(y_size))
    t_model.compile(loss='mean_squared_error', optimizer=RMSprop(lr=0.004), metrics=[metrics.mae])
    return t_model
model = model(arr_x_train.shape[1], 1)
#model.summary()

# Epoch and Batch Size
epochs = 800
batch_size = 128

# Tensoboard Logic
LOG_DIR = os.getcwd()
tensorboard = TensorBoard(log_dir='./LOG_DIR', histogram_freq=0, write_graph=True, write_images=True)

# Fit the Model
history = model.fit(arr_x_train, arr_y_train, batch_size=batch_size, epochs=epochs, shuffle=True, verbose=2,
                    callbacks=[tensorboard], validation_data=(arr_x_valid, arr_y_valid),)
train_score = model.evaluate(arr_x_train, arr_y_train, verbose=0)
valid_score = model.evaluate(arr_x_valid, arr_y_valid, verbose=0)
print('Train MAE: ', round(train_score[1], 4), ', Train Loss: ', round(train_score[0], 4))
print('Val MAE: ', round(valid_score[1], 4), ', Val Loss: ', round(valid_score[0], 4))
print(os.getcwd())

# Function to Plot the Loss
def plot_loss(h):
    plt.figure()
    plt.plot(h['loss'])
    plt.plot(h['val_loss'])
    plt.title('Training vs Validation Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Validation'])
    plt.draw()
    plt.show()
    return
plot_loss(history.history)