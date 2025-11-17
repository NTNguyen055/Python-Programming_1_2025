import numpy as np

x = np.array([1, 2])        # Tạo mảng với số nguyên → NumPy tự chọn kiểu int mặc định
print(x.dtype)              # In kiểu dữ liệu của mảng (thường là int32 hoặc int64 tùy hệ thống)

x = np.array([1.0, 2.0])    # Tạo mảng với số thực → NumPy tự chọn kiểu float64
print(x.dtype)              # In kiểu dữ liệu: float64

x = np.array([1, 2], dtype=np.int64)  # Tạo mảng và chỉ định rõ kiểu dữ liệu là int64
print(x.dtype)                        # In kiểu dữ liệu: int64
