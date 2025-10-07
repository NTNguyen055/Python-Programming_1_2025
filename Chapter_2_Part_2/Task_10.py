# Viết Chương trình nhập các số từ bàn phím. In ra giá trị trung bình

totol = 0   
count = 0

while True:

    inp = input("Nhập vào một số (hoặc nhập 'Done' để kết thúc): ")

    if inp == 'Done':
        break

    value = float(inp)
    total += value
    count += 1

average = total / count
print("Giá trị trung bình là:", average)