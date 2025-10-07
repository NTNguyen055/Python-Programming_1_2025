# Tạo một chương trình đọc các từ của người dùng cho đến khi người dùng nhập vào một dòng trống.
# Sau khi người dùng nhập vào một dòng trống, chương trình sẽ hiển thị từng từ do người dùng nhập sau khi loại bỏ từ bị trùng. 
# Các từ phải được hiển thị theo thứ tự mà chúng được nhập vào. 

def read_unique_words():
    words = []        
    seen = set()      # dùng để kiểm tra trùng lặp nhanh

    print("Nhập các từ (nhập dòng trống để kết thúc):")
    while True:
        word = input().strip()
        if word == "":  
            break

        if word not in seen:
            words.append(word)   
            seen.add(word)       # đánh dấu đã gặp

    print("\nCác từ không trùng (theo thứ tự nhập):")
    for w in words:
        print(w)

read_unique_words()
