# Viết một chương trình kiểm tra một chuỗi nhập vào từ bàn phím: Chuỗi hoa; Chuỗi thường; Chuỗi chứa ký tự hoa và ký tự thường.

st = input("Nhập chuỗi: ")

if st.isupper():
    print("Chuỗi hoa")

elif st.islower():
    print("Chuỗi thường")

else:  
    print("Chuỗi chứa ký tự hoa và ký tự thường")