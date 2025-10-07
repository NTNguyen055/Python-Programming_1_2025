# Sử dụng cấu trúc từ điển, viết một chương trình nhập một câu, in số chữ hoa và số chữ thường trong câu đó.

input_str = input("Nhập vào một chuỗi: ")

d = {'CHỮ HOA':0, 'CHỮ THƯỜNG':0}

for char in input_str:

    if char.isupper():
        d['CHỮ HOA'] += 1

    elif char.islower():
        d['CHỮ THƯỜNG'] += 1   

print("Số chữ hoa là: ", d['CHỮ HOA'])
print("Số chữ thường là: ", d['CHỮ THƯỜNG'])