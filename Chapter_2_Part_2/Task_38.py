# Tạo một chương trình đọc số nguyên từ người dùng cho đến khi một dòng trống được nhập. 
# Khi tất cả các số nguyên đã được đọc, chương trình sẽ hiển thị theo quy tắt: 
# tất cả các số âm, theo sau là tất cả các số không, theo sau là tất cả các số dương. 
# Trong mỗi nhóm, các số phải được hiển thị theo cùng thứ tự mà người dùng đã nhập. 

def group_numbers():
    negatives = []  
    zeros = []      
    positives = []  

    print("Nhập các số nguyên (nhập dòng trống để kết thúc):")
    while True:
        line = input().strip()
        if line == "":   # dừng khi nhập dòng trống
            break
        try:
            num = int(line)
            if num < 0:
                negatives.append(num)
            elif num == 0:
                zeros.append(num)
            else:
                positives.append(num)
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")

    print("\nKết quả theo quy tắc:")
    for n in negatives:
        print(n)
    for n in zeros:
        print(n)
    for n in positives:
        print(n)


# Gọi hàm
group_numbers()
