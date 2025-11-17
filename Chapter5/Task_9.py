import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)  # Tạo ma trận x 2x2 kiểu float64
y = np.array([[5,6],[7,8]], dtype=np.float64)  # Tạo ma trận y 2x2 kiểu float64

print(x + y)               # Cộng từng phần tử của 2 ma trận (element-wise)
print(np.add(x, y))        # Hàm tương đương: np.add thực hiện cộng element-wise

print(x - y)               # Trừ từng phần tử của 2 ma trận (element-wise)
print(np.subtract(x, y))   # Hàm tương đương: np.subtract

print(x * y)               # Nhân từng phần tử (element-wise), KHÔNG phải nhân ma trận
print(np.multiply(x, y))   # Hàm tương đương: np.multiply

print(x / y)               # Chia từng phần tử (element-wise)
print(np.divide(x, y))     # Hàm tương đương: np.divide

print(np.sqrt(x))          # Lấy căn bậc 2 từng phần tử của ma trận x
