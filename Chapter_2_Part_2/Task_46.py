# Định nghĩa một hàm có thể tạo ra một danh sách chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20)
# rồi in 5 phần tử cuối cùng trong danh sách. 

def power_5end_display():

    l = list()
    for i in range(1, 21):
        l.append(i**2)

    print(f"Danh sách 5 phần tử đầu tiên: {l[-5:]}")

power_5end_display()

