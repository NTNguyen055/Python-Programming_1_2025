#  Viết một chương trình tính và in kết quả giai thừa của một số nhập vào từ bàn phím

n = int(input("Nhập một số nguyên dương: "))

def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)
    
print(f"Giai thừa của {n} là: {giai_thua(n)}")