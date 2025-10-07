# Hiển thị 10 từ có tuần suất xuất hiện nhiều nhất
# (phổ biến nhất) trong file romeo.txt

ftext = open("romeo.txt")
dict = {}

for word in ftext:
    word_list = word.split()
    for tu in word_list:
        dict[tu] = dict.get(tu, 0) + 1

list = []
for key, val in dict.items():
    newtup = (val, key) 
    list.append(newtup)

list = sorted(list, reverse=True)

for val, key in list[:10] :
    print(key, val)
