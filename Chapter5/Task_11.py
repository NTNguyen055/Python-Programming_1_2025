import numpy as np

x = np.array([[1,2],[3,4]])  
print(np.sum(x))           # Tổng tất cả phần tử trong ma trận x: 1+2+3+4 = 10
print(np.sum(x, axis=0))  # Tổng theo cột (axis=0): [1+3, 2+4] = [4, 6]
print(np.sum(x, axis=1))  # Tổng theo hàng (axis=1): [1+2, 3+4] = [3, 7]

x = np.array([[1,2], [3,4]])
print(x)                   # In ma trận x
print(x.T)                 # Chuyển vị ma trận: hàng thành cột, kết quả [[1,3],[2,4]]

v = np.array([1,2,3])
print(v)                   # In vector v (1D array): [1,2,3]
print(v.T)                 # Chuyển vị của vector 1D vẫn là vector 1D, in ra vẫn [1,2,3]
