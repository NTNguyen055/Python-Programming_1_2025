# Định nghĩa một hàm có thể tạo và in danh sách chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20). 
# Yêu cầu: Sử dụng toán tử ** để lấy giá trị bình phương; Sử dụng range() cho vòng lặp; 
# Sử dụng list.append() để thêm giá trị vào danh sách.

def power_display():

    l = list()

    for i in range(1, 21):
        l.append(i**2)
    
    print(f"Danh sách các giá trị bình phương: {l}")

power_display()

        