# Viết một chương trình xác định tốc độ di chuyển của một vật khi nó chạm đất.
# Người dùng sẽ nhập chiều cao mà từ đó vật đó được thả (đơn vị tính mét (m)).
# v_i tốc độ ban đầu, a là gia tốc trọng trường, và d là độ cao. Tốc độ ban đầu của một vật là 0 m/s,  gia tốc trọng trường là 9,8 m/s2.


import math

d = float(input("Nhập chiều cao (m): "))

v_i = 0  # Vận tốc ban đầu (m/s)
a = 9.81  # Gia tốc trọng trường (m/s^2)   

v_f = math.sqrt(math.pow(v_i, 2) + 2 * a * d)

print(f"Tốc độ của vật khi chạm đất là: {v_f} m/s")
