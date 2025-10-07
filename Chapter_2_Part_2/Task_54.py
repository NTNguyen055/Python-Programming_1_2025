# Khi viết ra một danh sách các từ bằng tiếng Anh, người ta thường phân tách các từ bằng dấu phẩy. 
# Ngoài ra, thêm từ “and” trước từ cuối cùng, trừ khi danh sách chỉ chứa một từ.

def format_words(words):
    if not words:  # nếu danh sách rỗng
        return ""
    
    elif len(words) == 1:
        return words[0]
    
    elif len(words) == 2:
        return words[0] + " and " + words[1]
    
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

def main():
    print("Nhập các từ tiếng Anh (nhập xong bấm Enter 2 lần để kết thúc):")
    words = []

    while True:
        word = input("Nhập từ: ").strip()
        if word == "":
            break
        words.append(word)

    result = format_words(words)
    print("\nDanh sách đã định dạng:")
    print(result)

if __name__ == "__main__":
    main()
