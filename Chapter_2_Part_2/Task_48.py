# Viết hàm có 03 tham số và trả về giá trị trung bình của các tham số đó. 
# Bao gồm một chương trình chính đọc ba giá trị từ người dùng và hiển thị giá trị trung bình của chúng.

def average_of_three(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def main():
    x = float(input("Nhập số thứ nhất: "))
    y = float(input("Nhập số thứ hai: "))
    z = float(input("Nhập số thứ ba: "))

    avg = average_of_three(x, y, z)
    print(f"Giá trị trung bình của {x}, {y}, {z} là: {avg}")


# Gọi hàm main
if __name__ == "__main__":
    main()
