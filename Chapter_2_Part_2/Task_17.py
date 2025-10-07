# Sử dụng cấu trúc từ điển, viết một chương trình nhập một câu, in số chữ cái và chữ số trong câu đó

input_str = input("Nhập vào một chuỗi: ")

d = {'CHỮ CÁI':0, 'CHỮ SỐ':0}

for char in input_str:

    if char.isalpha():
        d['CHỮ CÁI'] += 1

    elif char.isdigit():
        d['CHỮ SỐ'] += 1

print("Số chữ cái là: ", d['CHỮ CÁI'])
print("Số chữ số là: ", d['CHỮ SỐ'])


