# Viết chương trình đọc một chuỗi từ người dùng và sử dụng một vòng lặp để xác định xem đó có phải là một Palindrom hay không. 
# Hiển thị kết quả, bao gồm một thông báo đầu ra có ý nghĩa.

def Check_palidrom(text):

    is_palidrom = True
    for i in range(len(text) // 2):
        if text[i] != text[-(i + 1)]:
            is_palidrom = False
            break

    if is_palidrom:
        print(f"{text} là một Palindrom.")

    else:
        print(f"{text} không phải là một Palindrom.")

s = input("Nhập một chuỗi: ")
text = s.replace(" ", "").lower()

Check_palidrom(text)

