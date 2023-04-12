import numpy as np

def step(x):
    y = x > 0
    return y.astype(int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)

def relu(x):
    return np.maximum(x, 0)

def identity(x):
    return x

def softmax(x):
    if x.ndim == 2:
        x = x.T
        c = np.max(x, axis=0)
        y = np.exp(x - c) / np.sum(np.exp(x - c), axis=0)
        return y.T 
    
    c = np.max(x)
    y = np.exp(x - c) / np.sum(np.exp(x - c), axis=0)
    return y

def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7

    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size