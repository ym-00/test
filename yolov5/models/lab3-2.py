from tensorflow.keras.datasets import mnist
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(f"Train dataset shape {X_train.shape}")
print(f"Test dataset shape, {X_test.shape}")

rows, cols = 3, 3
fig, axs = plt.subplots(rows, cols, figsize = (6, 6))
for i in range(rows):
    for j in range(cols):
        axs[i][j].imshow(X_train[cols*i + j], cmap='gray')
plt.show()