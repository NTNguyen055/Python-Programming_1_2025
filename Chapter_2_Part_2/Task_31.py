# Viết chương trình thực hiện mật mã Caesar, cho phép người dùng nhập vào một tin nhắn và sau đó hiển thị tin nhắn đã được mã hóa. 
# Đảm bảo rằng chương trình mã hóa cả chữ hoa và chữ thường

# Chương trình mã hóa Caesar
def caesar_encrypt(message, shift):

    encrypted = ""
    for char in message:
        if char.isalpha():  # Nếu là chữ cái
            base = ord('A') if char.isupper() else ord('a')

            # Dịch chuyển trong phạm vi 26 ký tự
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Ký tự khác giữ nguyên (dấu cách, số, dấu câu...)
            encrypted += char
    return encrypted

# Nhập dữ liệu từ người dùng
msg = input("Nhập dữ liệu cần mã hóa: ")
shift = 3

# Mã hóa và in kết quả
encrypted_msg = caesar_encrypt(msg, shift)
print("Dữ liệu đã mã hóa:", encrypted_msg)
