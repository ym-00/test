import pandas as pd
import numpy as np

diabetes_df=pd.read_csv('diabetes.csv')






# X=np.asarray(diabetes_df.drop('Pregnancies',axis=1))
#
# y=np.asarray(diabetes_df.Pregnancies)
#
# print(X,y)
#
# from sklearn import preprocessing
# min_max_scaler = preprocessing.MinMaxScaler()
# X_scaled = min_max_scaler.fit_transform(X)
# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test=train_test_split(X_scaled,y,test_size=0.1,random_state=1)
#
# from tensorflow.keras.utils import to_categorical
# y_train_one_hot=to_categorical(y_train,num_classes=2)
# y_test_one_hot=to_categorical(y_test,num_classes=2)