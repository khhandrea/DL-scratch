import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

print(f'a : {a}')
print(f'b : {b}')
print()

print(f'a + b : {a + b}')
print(f'a - b : {a - b}')
print(f'a * b : {a * b}')
print(f'a / b : {a / b}')
print()

big = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])
print(f'big : {big}')
print(f'broadcasting a + big = {a + big}')