# Định nghĩa một hàm có đầu vào là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển. 
# Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng.

def compare_strings(str1, str2):

    if len(str1) > len(str2):
        print("Chuỗi 1 dài hơn: " + str1)

    elif len(str1) < len(str2):
        print("Chuỗi 2 dài hơn: " + str2)

    else:
        print("Hai chuỗi có độ dài bằng nhau:")
        print(str1)
        print(str2)
