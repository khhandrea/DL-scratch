import numpy as np

def identity(x):
    return x

def softmax(x):
    c = np.max(x)
    np.exp(x - c) / np.sum(np.exp(x - c))