# Viết một chương trình có thể tính giai thừa của một số cho trước. 
# Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320. 
# Yêu cầu: định nghĩa hàm tính giai thừa

def factorial(n: int) -> int:
    
    # Hàm tính giai thừa của số nguyên dương n
    if n < 0:
        raise ValueError("Không có giai thừa cho số âm")
    result = 1

    for i in range(1, n+1): # i = 1 và i chạy từ 1 - n
        result *= i
    return result


# Chương trình chính
n = int(input("Nhập số nguyên n: "))
print(f"Giai thừa của {n} là: {factorial(n)}")
