import numpy as np 

a = np.array([1, 2, 3])  # Tạo mảng NumPy 1 chiều gồm 3 phần tử

print(type(a))  # In ra kiểu dữ liệu của 'a' (ndarray của NumPy)
print(a.shape)  # In ra kích thước của mảng (3,) nghĩa là có 3 phần tử theo 1 chiều
print(a[0], a[1], a[2])  # Truy cập và in các phần tử của mảng: 1, 2, 3

a[0] = 5  # Gán lại giá trị phần tử đầu tiên của mảng thành 5
print(a)  # In lại mảng sau khi cập nhật: [5 2 3]

b = np.array([[1,2,3],[4,5,6]])  # Tạo mảng 2 chiều (ma trận 2x3)

print(b.shape)  # In kích thước của mảng 2D: (2, 3) nghĩa là 2 hàng, 3 cột
print(b[0, 0], b[0, 1], b[1, 0])  # Truy cập phần tử: b[row, column]
                                 # b[0,0] = 1, b[0,1] = 2, b[1,0] = 4
