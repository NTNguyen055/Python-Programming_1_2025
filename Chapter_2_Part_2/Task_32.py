# Mở rộng viết chương trình mã hóa mã Caesar, cho phép người dùng cung cấp tin nhắn và sau đó hiển thị tin nhắn đã được mã hóa. 
# Chương trình cũng hỗ trợ giải mã (chuyển ngược lại) để có thể sử dụng cả hai chức năng: mã hóa tin nhắn và giải mã tin nhắn. 
# Và số ký tự dịch chuyển do người dùng nhập.

# Chương trình Caesar Cipher: Mã hóa & Giải mã

def caesar_cipher(message, shift, mode="encrypt"):

    result = ""
    if mode == "decrypt":
        shift = -shift  # Đảo chiều để giải mã

    for char in message:
        if char.isalpha():  # Nếu là chữ cái
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Ký tự khác giữ nguyên
    return result


# --- Giao diện chương trình ---
print("=== Chương trình Caesar Cipher ===")
choice = input("Bạn muốn (e)ncrypt - mã hóa hay (d)ecrypt - giải mã? (e/d): ").strip().lower()

message = input("Nhập dữ liệu của bạn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))

if choice == "e":
    encrypted = caesar_cipher(message, shift, mode="encrypt")
    print("Dữ liệu đã mã hóa:", encrypted)

elif choice == "d":
    decrypted = caesar_cipher(message, shift, mode="decrypt")
    print("Dữ liệu đã giải mã:", decrypted)

else:
    print("Lựa chọn không hợp lệ!")
