# Với số nguyên n nhất định, hãy viết chương trình tạo ra một dictionary chứa (i, i*i) 
# với i là số nguyên từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này.

n = int(input("Nhập số nguyên n: "))
result = {i: i*i for i in range(1, n+1)}
print(result)
