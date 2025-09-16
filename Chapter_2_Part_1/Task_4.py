# Viết một chương trình thay thế một từ trong chuỗi. Yêu cầu: 
# Nhập vào một chuỗi 
# Nhập vào một từ cần thay thế và một từ thay thế. 
# Sau đó, hiển thị kết quả ra màn hình.

st1 = input("Enter first string: ")

st2 = input("Enter the word to replace: ")

st3 = input("Enter the replacement word: ")

st1 = st1.replace(st2, st3)

print("Updated string:", st1)