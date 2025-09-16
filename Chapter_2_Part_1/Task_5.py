# Viết một chương trình nhập vào 1 chuỗi. Sau đó, xuất ra màn hình: 
# 5 ký tự cuối cùng; 5 ký tự đầu tiên. 
# 4 chuỗi trên một dòng cách 1 khoảng trắng.
# 4 chuỗi trên 4 dòng.

st = input("Enter a string: ")

first_five_chars = st[:5]
end_five_chars = st[-5:]
fourth_str_1_line = 4 * (st + " ")
fourth_str_4_line = 4 * (st + "\n")

print("First five characters:", first_five_chars)
print("Last five characters:", end_five_chars)
print("Fourth string (1 line):", fourth_str_1_line)
print("Fourth string (4 lines):", fourth_str_4_line)
