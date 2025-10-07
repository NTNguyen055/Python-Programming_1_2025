# Viết chương trình nhập vào 1 số, cho biết số đó có phải là số Amstrong hay không?

n = int(input("Nhập vào một số: "))
level = int(input("Nhập vào bậc của số: "))

# Kiểm tra số Amstrong
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** level
    temp //= 10

if n == sum:
    print(n, "là số Amstrong bậc " + str(level))
else:
    print(n, "không phải là số Amstrong bậc " + str(level))
