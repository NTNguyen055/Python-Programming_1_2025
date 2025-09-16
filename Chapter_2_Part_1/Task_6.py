# Viết chương trình tính thể tích hình trụ V = πr2h với r là bán kính của mặt đáy, h là chiều cao của hình trụ, và π là hằng số pi. 
# Với r và h nhập vào từ bàn phím.

import math

r = float(input("Nhập bán kính đáy r = ")) # Bán kính đáy
h = float(input("Nhập chiều cao h = ")) # Chiều cao

V = math.pi * r**2 * h # Công thức tính thể tích hình trụ V = πr^2h

print("Thể tích hình trụ là V =", V)
