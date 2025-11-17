import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])  # Ma trận 4x3
v = np.array([1, 0, 1])                                  # Vector 3 phần tử

vv = np.tile(v, (4, 1))   # Nhân bản vector v 4 lần theo hàng, tạo ma trận 4x3
print(vv)                  # In ma trận vv: mỗi hàng giống vector v

y = x + vv                # Cộng ma trận x với vv (element-wise)
print(y)                  # In kết quả: tương đương với việc cộng v với từng hàng của x
