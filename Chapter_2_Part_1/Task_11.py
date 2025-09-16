# Viết chương trình đọc chiều dài và chiều rộng của một cánh đồng từ người dùng. 
# Hiển thị diện tích của cánh đồng theo theo đơn vị tính là Mẫu Anh. 
# Gợi ý: Một Mẫu Anh bằng 43.560 met vuông

length = float(input("Nhập chiều dài cánh đồng (mét): "))
width = float(input("Nhập chiều rộng cánh đồng (mét): "))

S = length * width

print(f"Diện tích cánh đồng là: {S / 43560} Mẫu Anh")

