# Viết một chương trình nhập vào một số nguyên dương. 
# Nếu nó là số chẵn thì in ra chuỗi “Đây là số chẵn”, ngược lại thì in ra chuỗi “Đây là số lẻ”:

n = int(input("Nhập một số nguyên dương: "))

if n % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")
