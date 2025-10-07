# Viết một chương trình tạo ra một danh sách các số lẻ từ các số được người dùng nhập vào. 
# Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9

def is_odd():
    
    numbers = list()

    while True:
        inp = input("Nhập vào một số (hoặc nhập 'Done' để kết thúc): ").lower()
        if inp == 'done': break

        num = int(inp)
        if num % 2 != 0:
            numbers.append(num)

    print("Danh sách các số lẻ là: ")
    print(numbers)
    
is_odd()
