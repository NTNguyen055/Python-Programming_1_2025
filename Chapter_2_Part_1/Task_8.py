# Viết chương trình tính diện tích tam giác đều theo định lý Heron. Yêu cầu nhập vào cạnh tam giác đều.
# Yêu cầu nhập vào cạnh tam giác đều.

import math

a = float(input("Nhập độ dài cạnh tam giác đều: "))

# Tính diện tích tam giác đều theo định lý Heron
S = (math.sqrt(3) / 4) * a * a

print(f"Diện tích tam giác đều với cạnh {a} là: {S:.2f}")

