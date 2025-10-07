# Viết chương trình chuyển đổi số thập phân thành nhị phân. Đọc số thập phân từ người dùng dưới dạng số nguyên. 
# Hiển thị kết quả, cùng với một thông điệp thích hợp.

def is_binary(n):

    num = n
    binary = ""

    if num == 0:
        binary = "0"
    
    else:
        while num > 0:
            temp = num % 2
            binary = str(temp) + binary
            num = num // 2
    
    print(f"Số {n} trong hệ nhị phân là: {binary}")

n = int(input("Nhập 1 số nguyên dương lớn hơn 0: "))

is_binary(n)
