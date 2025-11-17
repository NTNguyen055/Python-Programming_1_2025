import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])  # Ma trận 4x3
v = np.array([1, 0, 1])                                  # Vector 3 phần tử

y = np.empty_like(x)  # Tạo ma trận rỗng cùng shape với x, để lưu kết quả

for i in range(4):
    y[i, :] = x[i, :] + v   # Cộng vector v với từng hàng của x và lưu vào y

print(y)  # In ma trận y sau khi cộng: mỗi hàng của y = hàng tương ứng của x + v
