# Viết một chương trình tìm tất cả các số trong đoạn 100 và 300 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn. 
# In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng. 

even_numbers = []

for num in range(100, 301):

    str_num = str(num)

    if (int(str_num[0]) % 2 == 0 and 
        int(str_num[1]) % 2 == 0 and 
        int(str_num[2]) % 2 == 0):

        even_numbers.append(str_num)

print(",".join(even_numbers))