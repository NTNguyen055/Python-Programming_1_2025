# Viết một chương trình để tạo tuple chứa các phần tử là số chẵn từ một tuple (1,2,3,4,5,6,7,8,9,10) cho trước. 

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_t = tuple(i for i in t if i % 2 == 0)

print(f"Tuple chứa các số chắn là : {even_t}")

t.index()