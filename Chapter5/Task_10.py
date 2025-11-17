import numpy as np

x = np.array([[1,2],[3,4]])    # Ma trận 2x2
y = np.array([[5,6],[7,8]])    # Ma trận 2x2
v = np.array([9,10])           # Vector 2 chiều
w = np.array([11, 12])         # Vector 2 chiều

print(v.dot(w))                # Tích vô hướng (dot product) giữa 2 vector: 9*11 + 10*12
print(np.dot(v, w))            # Hàm tương đương: np.dot

print(x.dot(v))                # Nhân ma trận x với vector v (matrix-vector multiplication)
print(np.dot(x, v))            # Kết quả tương đương: np.dot(x, v)

print(x.dot(y))                # Nhân ma trận (matrix-matrix multiplication)
print(np.dot(x, y))            # Hàm tương đương: np.dot(x, y)
