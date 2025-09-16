# Viết một chương trình đọc hai số nguyên a và b từ người dùng. 
# Chương trình sẽ tính toán và hiển thị:

import math

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# - Tổng của a và b
sum = a + b
print(f"Tổng của {a} và {b} là: {sum}")

# - Hiệu của a và b
dif = a - b
print(f"Hiệu của {a} và {b} là: {dif}")

# - Tích của a và b
multi = a * b
print(f"Tích của {a} và {b} là: {multi}")

# - Thương của a và b
if b != 0:
    div = a / b
    print(f"Thương của {a} và {b} là: {div}")
else:
    print("Không thể chia cho 0.")

# - Tính a mod b
if b != 0:
    mod = a % b
    print(f"{a} mod {b} là: {mod}")

else:
    print("Không thể tính mod khi b là 0.")

# - Tính log10 của a (nếu a > 0)
if a > 0:
    log_a = math.log10(a)
    print(f"log10 của {a} là: {log_a}")

else:
    print("Không thể tính log10 khi a không lớn hơn 0.")

# - Tính a lũy thừa b (a^b)
if b != 0:
    power = math.pow(a, b)
    print(f"{a} lũy thừa {b} là: {power}")

else:
    print("Không thể tính lũy thừa khi b là 0.")
