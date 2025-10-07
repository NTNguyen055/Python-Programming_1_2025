#  Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một chương trình in một nửa phần tử đầu tiên trong 1 dòng 
# và 1 nửa phần tử còn lại trong 1 dòng

# Khai báo tuple
t = (1,2,3,4,5,6,7,8,9,10)

# Tìm vị trí giữa
mid = len(t) // 2

# In nửa đầu
print(t[:mid])

# In nửa sau
print(t[mid:])
