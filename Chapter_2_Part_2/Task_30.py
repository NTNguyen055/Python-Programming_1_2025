# Viết chương trình đọc một năm từ người dùng và hiển thị thông báo cho biết đó có phải là năm nhuận hay không

def leap_year(y):
    
    if (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
        print(f"Năm {y} là năm nhuận.")

    else:
        print(f"Năm {y} là năm không nhuận.")

y = int(input("Nhập vào một năm ngẫu nhiên: "))
leap_year(y)