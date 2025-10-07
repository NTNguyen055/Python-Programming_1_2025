# Viết một hàm trả về một danh sách chứa mọi danh sách con có thể có của danh sách. 
# Ví dụ: danh sách con của [1, 2, 3] là [], [1], [2], [3], [1, 2], [2, 3] và [1, 2, 3].

def all_sublists(lst):
    sublists = [[]]  # Đảm bảo luôn có sublist rỗng
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n+1):
            sublists.append(lst[i:j])
    return sublists

def main():
    data = [1, 2, 3]
    result = all_sublists(data)
    print("Các sublist của", data, "là:")
    for sub in result:
        print(sub)

if __name__ == "__main__":
    main()
