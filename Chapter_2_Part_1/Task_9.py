# Chạy chương trình Bài 7, nhập giá trị cho trường hợp tam giác đều (lưu ý: giá trị cạnh tam giác = giá trị cạnh tam giác Bài 8). 
# Đánh giá kết quả khi chạy chương trình Bài 7 và Bài 8

import math


a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

# Nhập các góc A, B, C
A = float(input("Nhập góc A (độ): "))
B = float(input("Nhập góc B (độ): "))
C = float(input("Nhập góc C (độ): "))

# Chuyển đổi góc từ độ sang radian
A_rad = math.radians(A)
B_rad = math.radians(B)
C_rad = math.radians(C)

# Tính diện tích tam giác
S1 = 0.5 * a * b * math.sin(C_rad)
S2 = 0.5 * b * c * math.sin(A_rad)
S3 = 0.5 * a * c * math.sin(B_rad)

print(f"Diện tích tam giác tính theo công thức 1/2 * a * b * sinC: {S1:.2f}")
print(f"Diện tích tam giác tính theo công thức 1/2 * b * c * sinA: {S2:.2f}")
print(f"Diện tích tam giác tính theo công thức 1/2 * a * c * sinB: {S3:.2f}")

# Kiểm tra giá trị chung

S = (S1 + S2 + S3) / 3
print(f"Diện tích tam giác (giá trị chung): {S:.2f}")


# Sau khi test với tam giác đều (a = b = c), ta thấy kết quả diện tích từ cả hai chương trình đều giống nhau.