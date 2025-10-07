# Định nghĩa một hàm có đầu vào là 2 chuỗi và in chuỗi có độ dài lớn hơn. 
# Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng. Sử dụng hàm len() để lấy chiều dài của một chuỗi.

def compare_strings(s1: str, s2: str):
    if len(s1) > len(s2):
        print("Chuỗi dài hơn là:", s1)
    elif len(s2) > len(s1):
        print("Chuỗi dài hơn là:", s2)
    else:
        print("Hai chuỗi có cùng độ dài:")
        print(s1)
        print(s2)


# --- Chương trình chính ---
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

compare_strings(str1, str2)
