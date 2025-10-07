# Số nguyên tố là một số nguyên lớn hơn 1 và chỉ chia hết cho 1 và chính nó. 
# Viết hàm xác định tham số của nó có phải là số nguyên tố hay không, trả về True nếu đúng và False nếu không phải. 
# Viết chương trình chính đọc số nguyên từ người dùng và hiển thị thông báo cho biết đó có phải là số nguyên tố hay không.

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    # Chỉ cần kiểm tra đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    num = int(input("Nhập một số nguyên: "))

    if is_prime(num):
        print(f"{num} là số nguyên tố.")
    else:
        print(f"{num} không phải là số nguyên tố.")

# Gọi hàm main
if __name__ == "__main__":
    main()

