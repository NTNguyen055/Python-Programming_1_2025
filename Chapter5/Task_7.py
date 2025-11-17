import numpy as np

a = np.array([[1,2], [3,4], [5,6]])

bool_idx = (a > 2)     # Tạo mảng boolean: phần tử nào > 2 sẽ là True, còn lại False

print(bool_idx)        # In ra ma trận True/False tương ứng với điều kiện a > 2

print(a[bool_idx])     # Lọc và in ra các phần tử của a tại những vị trí có giá trị True

print(a[a > 2])        # Cách viết rút gọn tương đương: lấy các phần tử của a lớn hơn 2
