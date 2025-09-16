# Viết chương trình nhập chi phí của một bữa ăn tại nhà hàng từ người dùng. Chương trình sẽ tính thuế và tiền boa cho bữa ăn. 
# Trong đó, tiền boa là 18% số tiền bữa ăn (không có thuế); tiền thuế là 5% số tiền bữa ăn. 
# Đầu ra của chương trình là tổng tiền, gồm: thuế, số tiền boa và tiền bữa ăn. 
# Định dạng đầu ra sao cho tất cả các giá trị được hiển thị bằng hai con số thập phân

fee = float(input("Chi phí bữa ăn: "))

tip = fee * 0.18

tax = fee * 0.05

print(f"Tiền tip: {tip:.2f}")
print(f"Tiền thuế: {tax:.2f}")
print(f"Tổng tiền: {fee + tip + tax:.2f}")