# Viết chương trình loại bỏ các ký tự không phải là ký tự CHỮ CÁI và SỐ trong một chuỗi.

st_del = """!()-[]{};:""\,<>./?@#$%^&*_~"""

str_input = input("Nhập vào một chuỗi: ")

str_output = ""

for char in str_input:
    if char not in st_del:
        str_output += char
    
print("Chuỗi sau khi loại bỏ các ký tự không phải là ký tự CHỮ CÁI và SỐ là: ", str_output)
