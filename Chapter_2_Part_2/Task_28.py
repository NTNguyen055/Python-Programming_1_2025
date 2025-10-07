# Số ngày của một tháng thay đổi từ 28 đến 31 ngày. 
# Viết một chương trình đọc tên của một tháng từ người dùng dưới dạng một chuỗi. 
# Sau đó, chương trình sẽ hiển thị số ngày trong tháng đó (Chú ý: Số ngày là  28 hoặc 29 ngày để biểu diễn cho tháng 2).

def count_days_month(month):

    days_in_month = {
        "tháng 1": 31,
        "tháng 2": "28 hoặc 29",
        "tháng 3": 31,
        "tháng 4": 30,
        "tháng 5": 31,
        "tháng 6": 30,
        "tháng 7": 31,
        "tháng 8": 31,
        "tháng 9": 30,
        "tháng 10": 31,
        "tháng 11":  30,
        "tháng 12": 31
    }

    if month in days_in_month:
        print(f"Trong {month} có {days_in_month[month]} ngày.")
    
    else:
        print("Tên tháng không hợp lệ! Vui lòng nhập Tháng và 1 chữ số từ 1 - 12!")

month = input("Hãy nhập một tháng theo kiểu (Tháng 1, tháng 2,...): ")

count_days_month(month)