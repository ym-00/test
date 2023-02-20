import pandas as pd
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


diabetes_df=pd.read_csv('diabetes.csv')
X=np.asarray(diabetes_df.drop('Outcome',axis=1))
y=np.asarray(diabetes_df.Outcome)

from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.1,random_state=1)

from tensorflow.keras.utils import to_categorical
y_train_one_hot=to_categorical(y_train,num_classes=2)
y_test_one_hot=to_categorical(y_test,num_classes=2)


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
# define the keras model
model = Sequential()
model.add(Dense(40,input_dim=X_train.shape[1],activation='relu'))
model.add(Dense(20,activation='relu'))
model.add(Dense(2,activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics='accuracy')
history=model.fit(X_train, y_train_one_hot, epochs=80, batch_size=10,
          validation_split=0.1)

print((history.history.keys()))
from matplotlib import pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

