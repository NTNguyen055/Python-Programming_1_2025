# Viết chương trình tách từ thành 1 danh sách và sắp xếp các từ theo alphabe. 

str_input = input("Nhập vào một chuỗi: ")

list_words = str_input.split()

list_words.sort()  

print("Danh sách các từ sau khi sắp xếp theo alphabe: ")

for word in list_words:
    print(word)
