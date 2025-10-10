# Xử lý ngoại lệ FileNotFoundError:
# Lỗi này xuất hiện khi mở 1 file mà không tồn tại. Không tồn tại có thể do file chưa được tạo hoặc đường dẫn đến file không đúng.

from pathlib import Path

# Dùng Path để xác định đường dẫn tệp tương đối so với file .py hiện tại
filename = Path(__file__).parent / "ntnguyen.txt"

try:
    with open(filename) as f_file:
        contents = f_file.read()
except FileNotFoundError:
    msg = "File " + filename + " không tồn tại."
    print(msg)