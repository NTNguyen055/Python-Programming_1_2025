# Tạo ra một tự điển, có n phần tử, các khóa là từ 1 đến n và giá trị tương ứng là bình phương của khóa. 
# Sau đó in từ điển ra màn hình

import math

n = int(input("Nhập vào số phần tử n: "))

d = dict() # Tạo từ điển rỗng

for i in range(1, n + 1):

    d[i] =  math.pow(i, 2) # Gán giá trị bình phương của khóa i vào từ điển

print(d) # In từ điển ra màn hình
