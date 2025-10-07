# Viết một hàm có một tham số password để xác định xem mật khẩu có tốt hay không. 
# Một mật khẩu tốt là một mật khẩu dài ít nhất 8 ký tự và chứa ít nhất một chữ cái viết hoa, 
# ít nhất một chữ cái viết thường và ít nhất một số. Hàm sẽ trả về True nếu mật khẩu là tốt, ngược thì nó sẽ trả về Fales. 
# Chương trình có một chương trình chính đọc mật khẩu từ người dùng và hiển thị xem nó có tốt hay không.

def is_good_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit

def main():
    pwd = input("Nhập mật khẩu cần kiểm tra: ")
    if is_good_password(pwd):
        print("Mật khẩu TỐT")
    else:
        print("Mật khẩu KHÔNG TỐT")

# Gọi main
if __name__ == "__main__":
    main()
