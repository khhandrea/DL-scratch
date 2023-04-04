import numpy as np

def p_and(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    b = -0.7

    tmp = X @ W + b

    if tmp > 0:
        return 1
    else:
        return 0
    
def p_nand(x1, x2):
    X = np.array([x1, x2])
    W = np.array([-0.5, -0.5])
    b = 0.7

    tmp = X @ W + b

    if tmp > 0:
        return 1
    else:
        return 0
    
def p_or(x1, x2):
    X = np.array([x1, x2])
    W = np.array([0.5, 0.5])
    b = -0.2

    tmp = X @ W + b

    if tmp > 0:
        return 1
    else:
        return 0
    
def p_xor(x1, x2):
    s1 = p_nand(x1, x2)
    s2 = p_or(x1, x2)
    y = p_and(s1, s2)

    return y

    
print(f'p_and(0, 0) : {p_and(0, 0)}')
print(f'p_and(0, 1) : {p_and(0, 1)}')
print(f'p_and(1, 0) : {p_and(1, 0)}')
print(f'p_and(1, 1) : {p_and(1, 1)}')
print()

print(f'p_or(0, 0) : {p_or(0, 0)}')
print(f'p_or(0, 1) : {p_or(0, 1)}')
print(f'p_or(1, 0) : {p_or(1, 0)}')
print(f'p_or(1, 1) : {p_or(1, 1)}')
print()

print(f'p_nand(0, 0) : {p_nand(0, 0)}')
print(f'p_nand(0, 1) : {p_nand(0, 1)}')
print(f'p_nand(1, 0) : {p_nand(1, 0)}')
print(f'p_nand(1, 1) : {p_nand(1, 1)}')
print()

print(f'p_xor(0, 0) : {p_xor(0, 0)}')
print(f'p_xor(0, 1) : {p_xor(0, 1)}')
print(f'p_xor(1, 0) : {p_xor(1, 0)}')
print(f'p_xor(1, 1) : {p_xor(1, 1)}')
print()