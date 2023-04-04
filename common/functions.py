import numpy as np

def step(x):
    y = x > 0
    return y.astype(int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(x, 0)

def identity(x):
    return x

def softmax(x):
    c = np.max(x)
    y = np.exp(x - c) / np.sum(np.exp(x - c))

    return y

def softmax(x):
    if x.ndim == 2:
        x = x.T
        c = np.max(x, axis=0)
        y = np.exp(x - c) / np.sum(np.exp(x - c), axis=0)
        return y.T 
    
    c = np.max(x)
    y = np.exp(x - c) / np.sum(np.exp(x - c), axis=0)
    return y