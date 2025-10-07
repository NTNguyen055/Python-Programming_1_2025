# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5, nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). 
# Các số thu được sẽ được lưu vào 1 danh sách sau đó in thành chuỗi trên một dòng, cách nhau bằng dấu phẩy

numlist = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        numlist.append(str(num))
    
    print(','.join(numlist))