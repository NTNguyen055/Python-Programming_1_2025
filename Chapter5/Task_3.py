import numpy as np

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])  # Tạo ma trận 3x4

b = a[:2, 1:3]  # Lấy view gồm 2 hàng đầu và các cột 1→2 (không tạo bản sao, dùng chung dữ liệu với a)

print(a[0, 1])  # In giá trị a[0,1], ban đầu là 2

b[0, 0] = 77    # Thay đổi b[0,0], thực tế là thay đổi chính a[0,1] vì b là view của a

print(a[0, 1])  # In lại a[0,1], giá trị đã bị đổi thành 77 do sửa b
