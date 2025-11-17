import numpy as np  

a = np.zeros((2,2))  # Tạo mảng 2x2 toàn số 0
                     # Kết quả: [[0. 0.]
                     #           [0. 0.]]

b = np.ones((1,2))   # Tạo mảng 1x2 toàn số 1

c = np.full((2,2), 7)  # Tạo mảng 2x2 với toàn bộ phần tử có giá trị 7

d = np.eye(2)  # Tạo ma trận đơn vị 2x2 (đường chéo chính là 1, còn lại 0)
               # Kết quả: [[1. 0.]
               #           [0. 1.]]

e = np.random.random((2,2))  # Tạo mảng 2x2 với các số ngẫu nhiên từ 0 đến 1
