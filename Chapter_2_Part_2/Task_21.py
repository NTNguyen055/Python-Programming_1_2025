#  Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20). Sau đó thực thi hàm.$ 

def print_list():

    l = list ()
    for i in range(1, 21):
        l.append(i**2)

    print(l)

print_list()

