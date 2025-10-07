# Định nghĩa một hàm có thể tạo danh sách chứa giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20). 
# Sau đó in tất cả các giá trị của danh sách trừ 5 phần tử đầu tiên. 

def power_5thToEnd_display():

    l = list()
    for i in range(1, 21):
        l.append(i**2)

    print(f"Danh sách 5 phần tử đầu tiên: {l[5:]}")

power_5thToEnd_display()