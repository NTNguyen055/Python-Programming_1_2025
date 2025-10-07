# Viết chương trình nhập một chuỗi số, phân tách bằng dấu phẩy. In ra một danh sách và một tuple chứa mọi số.

str = input("Nhập vào một chuỗi số, phân tách bằng dấu phẩy: ")

numlist = str.split(',')
numtuple = tuple(numlist)

print("Danh sách:", numlist)
print("Tuple:", numtuple)