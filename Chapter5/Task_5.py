import numpy as np

a = np.array([[1,2], [3,4], [5,6]])   # Tạo ma trận 3x2

print(a[[0, 1, 2], [0, 1, 0]])        # Lấy các phần tử theo chỉ số tương ứng: (0,0), (1,1), (2,0)

print(np.array([a[0, 0], a[1, 1], a[2, 0]]))   # Cách viết tương đương: lần lượt lấy a[0,0], a[1,1], a[2,0]

print(a[[0, 0], [1, 1]])              # Lấy hai phần tử (0,1) và (0,1) → lặp lại cùng một giá trị

print(np.array([a[0, 1], a[0, 1]]))   # Cách viết tương đương: tạo mảng gồm 2 lần giá trị a[0,1]
