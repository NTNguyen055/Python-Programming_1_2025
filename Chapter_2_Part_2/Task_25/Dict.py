#  Tạo tệp tu_dien.py để định nghĩa:

# - 01 hàm Dict_Create(Max) để tạo 1 từ điển, chứa các key là số từ 1 đến Max (số Max nhập vào từ bàn phím) và các giá trị là bình phương của key. 
# - 01 Hàm Print_Item(d) để in các phần tử của từ điển.
# - 01 Hàm Print_Key(d) để in các giá trị của các phần tử từ điển
# - 01 Hàm Print_Value(d) để in giá trị của các phần tử từ điển 

def Dict_Create(Max):
    d = dict()
    for i in range(1, Max + 1):
        d[i] = i * i
    return d

def Print_Item(d):
    for item in d.items():
        print(item)

def Print_Key(d):
    for key in d.keys():
        print(key)

def Print_Value(d):
    for value in d.values():
        print(value)
