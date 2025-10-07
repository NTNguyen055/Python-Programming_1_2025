# Viết một chương trình đọc một chữ cái từ người dùng. 
# Nếu người dùng nhập a, e, i, o hoặc u thì chương trình hiển thị một thông báo cho biết rằng chữ cái đã nhập là nguyên âm (xét ngôn ngữ Anh).
# Nếu người dùng nhập y thì chương trình sẽ hiển thị một thông báo cho biết  có thể y là nguyên âm  hoặc phụ âm. 
# Nếu không phải các trường hợp trên, chương trình sẽ hiển thị một thông báo cho biết rằng chữ cái là phụ âm

def read_letter(letter):
    let = letter

    if let in ['a', 'e', 'i', 'o', 'u']:
        print("Chữ cái " + let + " đã nhập là nguyên âm!")

    elif let == 'y':
        print("Chữ cái " + let + " đã nhập là nguyên âm hoặc phụ âm!")

    else:
        print("Chữ cái " + let + " đã nhập là phụ âm!")

letter = input("Hãy nhập một chữ cái tiếng anh: ").lower()

while len(letter) > 1:
    letter = input("Lưu ý! Hãy nhập một chữ cái tiếng anh: ").lower()

read_letter(letter)

