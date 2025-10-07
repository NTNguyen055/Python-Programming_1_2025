# Viết một chương trình chấp nhận đầu vào là một câu, đếm số ký tự hoa, số ký tự thường. 

st = input("Nhập vào một chuỗi: ")

st_lower_char = 0
st_upper_char = 0

for char in st:

    if char.islower():
        st_lower_char += 1

    elif char.isupper():
        st_upper_char += 1

    else:
        pass

print(f"Số ký tự thường: {st_lower_char}")
print(f"Số ký tự hoa: {st_upper_char}")