import numpy as np

v = np.array([1,2,3])    # Vector v, shape (3,)
w = np.array([4,5])      # Vector w, shape (2,)

print(np.reshape(v, (3, 1)) * w)  
# Chuyển v thành cột (3x1) và nhân với w (1x2) → kết quả là outer product 3x2:
# [[1*4, 1*5],
#  [2*4, 2*5],
#  [3*4, 3*5]]

x = np.array([[1,2,3], [4,5,6]])  # Ma trận 2x3

print(x + v)  
# Cộng vector v (1D, shape (3,)) với mỗi hàng của x nhờ broadcasting
# Kết quả: [[2,4,6], [5,7,9]]

print((x.T + w).T)  
# Cách khác để cộng w (shape (2,)) với từng hàng của x:
# 1. Chuyển x thành x.T (shape 3x2)
# 2. Cộng w (shape (2,)) → broadcast theo cột
# 3. Chuyển lại T → shape 2x3
# Kết quả: [[1+4,2+4,3+4],[4+5,5+5,6+5]] = [[5,6,7],[9,10,11]]

print(x + np.reshape(w, (2, 1)))  
# Chuyển w thành cột (2x1) để broadcast theo hàng của x
# Kết quả tương tự ((x.T + w).T): [[5,6,7],[9,10,11]]

print(x * 2)  
# Nhân tất cả phần tử của x với 2 (element-wise multiplication)
# Kết quả: [[2,4,6],[8,10,12]]
