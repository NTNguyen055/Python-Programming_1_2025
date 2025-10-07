# Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1) với n là số nguyên được nhập vào (n> 0).

n = int(input("Nhập số nguyên dương n: "))

if n > 0:
    total = 0
    for i in range(1, n + 1):
        total += i / (i + 1)
    print(f"Tổng của chuỗi là: {total}")

else:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
