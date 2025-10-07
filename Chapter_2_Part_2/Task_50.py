# Viết hàm không có tham số để tạo mật khẩu ngẫu nhiên. Mật khẩu phải có độ dài ngẫu nhiên từ 7 đến 10 ký tự. 
# Mỗi ký tự phải được chọn ngẫu nhiên từ các vị trí 33 đến 126 trong bảng ASCII. Hàm sẽ trả về mật khẩu được tạo ngẫu nhiên.
# Hiển thị mật khẩu được tạo ngẫu nhiên trong chương trình chính.

import random

def generate_password() -> str:
    # Độ dài mật khẩu ngẫu nhiên từ 7 đến 10
    length = random.randint(7, 10)
    password = ""
    for _ in range(length):
        # Chọn ký tự ASCII ngẫu nhiên từ 33 đến 126
        char = chr(random.randint(33, 126))
        password += char
    return password

def main():
    pwd = generate_password()
    print("Mật khẩu ngẫu nhiên được tạo:", pwd)

# Gọi main
if __name__ == "__main__":
    main()
