import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])  # Tạo ma trận 4x3

print(a)  # In toàn bộ ma trận a

b = np.array([0, 2, 0, 1])  # Mỗi giá trị là chỉ số cột cần chọn cho từng hàng

print(a[np.arange(4), b])  
# Lấy phần tử ở từng hàng theo cột được chỉ định trong b:
# Hàng 0 → cột 0 → 1
# Hàng 1 → cột 2 → 6
# Hàng 2 → cột 0 → 7
# Hàng 3 → cột 1 → 11

a[np.arange(4), b] += 10  
# Cộng thêm 10 vào đúng các vị trí đã chọn ở trên

print(a)  
# In ma trận sau khi đã cộng 10 vào các vị trí được chọn
