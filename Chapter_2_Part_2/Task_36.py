# Viết chương trình đọc các số nguyên từ người dùng và lưu trữ chúng trong danh sách. 
# Chương trình sẽ tiếp tục đọc các giá trị cho đến khi người dùng nhập ký tự 0. 
# Sau đó, nó sẽ hiển thị tất cả các giá trị được nhập bởi người dùng (ngoại trừ 0) theo thứ tự tăng dần,
# với một giá trị xuất hiện trên mỗi dòng. 
# Sử dụng phương thức sắp xếp hoặc hàm được sắp xếp để sắp xếp danh sách.


def read_and_sort_numbers():
    numbers = []  # danh sách lưu các số

    while True:
        n = int(input("Nhập số nguyên (0 để dừng): "))
        if n == 0:
            break
        numbers.append(n)

    # Sắp xếp danh sách
    numbers.sort()

    # Hiển thị kết quả
    print("\nCác số đã nhập theo thứ tự tăng dần:")
    for num in numbers:
        print(num)


# Gọi hàm
read_and_sort_numbers()
