# Viết chương trình xác định tên của hình dạng dựa trên số cạnh của nó. 
# Ví dụ, nhập số 3 thì là hình tam giác, 4 hình tứ giác ,... 
# Yêu cầu: Chương trình hỗ trợ các hình dạng từ 3 đến 10 cạnh. 
# Nếu số cạnh vượt ra bên ngoài phạm vi này thì chương trình sẽ hiển thị thông báo lỗi thích hợp

def name_geometry(n):

    l = {
        3: "Hình tam giác",
        4: "Hình tứ giác",
        5: "Hình ngũ giác",
        6: "Hình lục giác",
        7: "Hình thất giác",
        8: "Hình bát giác",
        9: "Hình cửu giác",
        10: "Hình thập giác"
    }
    print(f"Số cạnh {n} tương ứng với " + l[n] + ".")

n = int(input("Nhập vào 1 số nguyên từ 3 - 10: "))

while (n < 3 or n > 10):
    n = int(input("Có lỗi! Hãy nhập vào 1 số nguyên từ 3 - 10: "))

name_geometry(n)
    