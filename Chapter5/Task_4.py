import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])  # Tạo ma trận 3x4

row_r1 = a[1, :]          # Lấy hàng thứ 1 dạng 1D array (vector hàng)
row_r2 = a[1:2, :]        # Lấy hàng thứ 1 nhưng dạng 2D array (ma trận con)

print(row_r1, row_r1.shape)  # In row_r1 và shape: (4,) → mảng 1 chiều
print(row_r2, row_r2.shape)  # In row_r2 và shape: (1,4) → mảng 2 chiều

col_r1 = a[:, 1]          # Lấy cột thứ 1 dạng 1D array (vector cột)
col_r2 = a[:, 1:2]        # Lấy cột thứ 1 nhưng dạng 2D array (ma trận con)

print(col_r1, col_r1.shape)  # In col_r1 và shape: (3,) → mảng 1 chiều
print(col_r2, col_r2.shape)  # In col_r2 và shape: (3,1) → mảng 2 chiều
