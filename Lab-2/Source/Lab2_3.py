import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.feature_extraction.text import CountVectorizer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential,Model
from keras.layers import Input,Dense, Embedding, LSTM, SpatialDropout1D,Dropout, Conv1D, GlobalMaxPooling1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
import re
from keras.optimizers import adam

data = pd.read_csv('spam.csv',encoding='latin-1')
# Keeping only the neccessary columns
data = data[['v2','v1']]

data['v2'] = data['v2'].apply(lambda x: x.lower())
data['v2'] = data['v2'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))



for idx, row in data.iterrows():
    row[0] = row[0].replace('rt', ' ')

max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(data['v2'].values)
X = tokenizer.texts_to_sequences(data['v2'].values)
print(X)
X = pad_sequences(X)
print(X)
embed_dim = 128

from sklearn.preprocessing import LabelEncoder

def createmodel():
     model = Sequential()
     model.add(Dense(512, activation='relu'))
     model.add(Dense(256, activation='tanh'))
     model.add(Dense(2, activation='softmax'))
     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
     return model
 #    model.summary()

labelencoder = LabelEncoder()
integer_encoded = labelencoder.fit_transform(data['v1'])
y = to_categorical(integer_encoded)
X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size = 0.33, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

batch_size = 32
model = createmodel()

#from tensorboard import *
#tbc = TensorBoardColab()
from keras.callbacks import TensorBoard
tensorboard = TensorBoard(log_dir="logs/{}",histogram_freq=0, write_graph=True, write_images=True)

model.fit(X_train, Y_train, epochs = 5, batch_size=batch_size, verbose = 2,callbacks=[tensorboard])
score,acc = model.evaluate(X_test,Y_test,verbose=2,batch_size=batch_size)

model.save('my_model.h5')
print(score)
print(acc)