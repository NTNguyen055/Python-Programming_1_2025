# Công thức năng lượng Q = M * C * DeltaT

M = float(input("Nhập khối lượng (M) tính bằng kg: "))
DeltaT = float(input("Nhập sự thay đổi nhiệt độ (DeltaT) tính bằng °C: "))

C = 4.186  # J/(g°C) - nhiệt dung riêng của nước
Q = M * C * DeltaT * 1000  # Chuyển đổi M từ kg sang g

print(f"Năng lượng cần thiết (Q) để thay đổi nhiệt độ là: {Q} J")
print("--------------------------------------------------")

# Tính toán chi phí khi thay đổi ΔT nhiệt độ của nước, biết rằng: chi phí là 8,9 cent mỗi kilowatt giờ, 1 Joules = 2.777e-7 kWh. 
# Hãy tính chi phí để nước đạt nhiệt độ như yêu cầu.

cost_per_kWh = 8.9  # cent

Q_kWh = Q * 2.777e-7  # Chuyển đổi Q từ Joules sang kWh
cost = Q_kWh * cost_per_kWh  # chi phí tính bằng cent

print(f"Đổi Q từ J sang kWh: {Q_kWh} kWh")
print(f"Chi phí để thay đổi nhiệt độ của nước là: {cost} cent")

