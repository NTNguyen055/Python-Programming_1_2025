# Một số nguyên, n, được cho là hoàn hảo khi tổng của tất cả các ước số của n bằng n. 
# Ví dụ, 28 là một số hoàn hảo vì các ước số của nó là 1, 2, 4, 7 và 14. Tổng 1 + 2 + 4 + 7 + 14 = 28. 
# Viết hàm xác định xem số nguyên dương có hoàn hảo hay không. 

def perfect_int (n: int) -> bool:
    
    if n <= 0:
        return False

    div_sum = 0

    for i in range(1, n):
        if n % i == 0:
            div_sum += i
    
    return div_sum == n

    # for i in range(1, n // 2 + 1):
    #     if n % i == 0:
    #         div_sum += i
    
    # return div_sum == n

def main():
    n = int(input("Nhập vào 1 số nguyên dương: "))
    if perfect_int(n):
        print(f"{n} là số hoàn hảo.")
    else:
        print(f"{n} không phải là số hoàn hảo")

    # print("Các số hoàn hảo trong khoảng từ 1 - 10000: ")
    # for n in range(1, 100001):
    #     if perfect_int(n):
    #         print(n)

if __name__ == "__main__":
    main()