# Viết Chương trình nhập các số từ bàn phím, các giá trị này lưu vào danh sách. Sau đó, in ra giá trị trung bình.

numlist = list()

while True:

    inp = input("Nhập vào một số (hoặc nhập 'Done' để kết thúc): ")

    if inp == 'Done': break

    Value = float(inp)
    numlist.append(Value)

average = sum(numlist) / len(numlist)

print("Giá trị trung bình là:", average)
print(numlist)


