import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
ex2_data=np.array([[  -3.29215704, -136.99048024],
       [   0.79952837,   -10.49591706],
       [  -0.93621395,   -4.73707511],
       [  -4.7226796 , -265.22306209],
       [  -3.60267397, -119.272012  ],
       [   4.93183364,  188.83658255],
       [  -0.85026525,   -16.38829193],
       [   2.45407162,   16.4067184 ],
       [   2.30965656,   -10.8807551 ],
       [   0.76820449,    -31.90269806],
       [   1.56786929,    1.82460014],
       [  -2.36282052,  -41.77705432],
       [  -0.28311318,   -6.15216134],
       [   1.63497495,   -23.91265665],
       [   0.6684103 ,   -3.67161635],
       [   0.99897702,   21.53401786],
       [  -2.48223722,  -44.70298567],
       [   2.61547479,   25.32459824],
       [   1.0607969 ,   -20.96435527],
       [   4.56228722,  148.94958177]])

#write your code here
plt.scatter(ex2_data[:,0],ex2_data[:,1])


X=ex2_data[:,0].reshape(20,1)

y=ex2_data[:,1].reshape(20,1)

model = linear_model.LinearRegression()

model.fit(X, y)
print('trained model parameters:', model.coef_, model.intercept_)#[[31.36320151]] [-25.86768743]

y_pred = model.predict(X)

train_mse = mean_squared_error(y[:, -1], y_pred)
train_r2s = r2_score(y[:, -1], y_pred)
print(train_mse,train_r2s)


from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

count = 1
results = []
for degree in [1,2,3,4,5]:
       polynomial_features = PolynomialFeatures(degree)  # n could be 1, 2, 3, 4,... (1 is for linear regression)
       X_poly = polynomial_features.fit_transform(X)  # X is the input data
       model_new = linear_model.LinearRegression()
       model_new.fit(X_poly, y)  # y is the output data
       print('trained model parameters:', model_new.coef_, model_new.intercept_)
       plt.plot(X_poly, model_new.predict(X_poly), label="degree %d" % degree)

plt.show()







