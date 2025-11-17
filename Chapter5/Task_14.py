import numpy as np

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])  # Ma trận 4x3
v = np.array([1, 0, 1])                                  # Vector 3 phần tử

y = x + v   # Cộng vector v với từng hàng của x nhờ broadcasting (không cần dùng vòng lặp hay tile)
print(y)    # In kết quả: mỗi hàng của y = hàng tương ứng của x + v