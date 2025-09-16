# Viết chương trình đọc một số nguyên dương n từ người dùng và sau đó hiển thị tổng của tất cả các số nguyên từ 1 đến n. 
# Tổng của n số nguyên dương đầu tiên có thể được tính bằng công thức:
# S = n * (n + 1) / 2

n = int(input("Nhập số nguyên dương n: "))

sum =  (n * (n + 1)) / 2

print(f"Tổng của tất cả các số nguyên từ 1 đến {n} là: {sum}")