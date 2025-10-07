# Định nghĩa một hàm có thể tạo danh sách chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20) 
# và in 5 phần tử đầu tiên trong danh sách. Yêu cầu: Sử dụng toán tử ** để lấy giá trị bình phương; 
# Sử dụng range() cho vòng lặp; Sử dụng list.append() để thêm phần tử vào danh sách; Sử dụng [n1:n2] để cắt danh sách.

def power_5th_display():

    l = list()
    for i in range(1, 21):
        l.append(i**2)

    print(f"Danh sách 5 phần tử đầu tiên: {l[:5]}")

power_5th_display()
