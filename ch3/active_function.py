from matplotlib import pyplot as plt
import numpy as np

def step(x):
    y = x > 0
    return y.astype(int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(x, 0)

plt.figure(figsize=(12, 4))

x = np.arange(-4, 4, 0.1)

y1 = step(x)
plt.subplot(1, 3, 1)
plt.title('step')
plt.plot(x, y1)

y2 = sigmoid(x)
plt.subplot(1, 3, 2)
plt.title('sigmoid')
plt.plot(x, y2)

y3 = relu(x)
plt.subplot(1, 3, 3)
plt.title('relu')
plt.plot(x, y3)

plt.show()