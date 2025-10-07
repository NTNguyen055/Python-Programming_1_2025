# Định nghĩa một hàm có thể tạo danh sách chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20) 
# và in 5 phần tử đầu tiên cùng với 5 phần tử cuối cùng trong danh sách.

def print_list():

    l = list ()

    for i in range(1, 21):
        l.append(i**2)

    print("5 phần tử đầu tiên:", l[:5])
    print("5 phần tử cuối cùng:", l[-5:])

print_list()
