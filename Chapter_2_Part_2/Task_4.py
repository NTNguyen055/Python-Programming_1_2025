# Viết chương trình in số lớn nhất của 3 số

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if (a > b) and (a > c):
    print(f"Số lớn nhất là: {a}")

elif (b > a) and (b > c):
    print(f"Số lớn nhất là: {b}")
    
else:
    print(f"Số lớn nhất là: {c}")
