# Xử lý ngoại lệ FileNotFoundError khi thực hiện chương trình đếm số từ trong file text

from pathlib import Path

def count_words_in_file(filename: str):
    path = Path(__file__).parent / filename
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại.")
    else:
        words = contents.split()
        print(f"File '{filename}' có {len(words)} từ.")

count_words_in_file("ntnguyen.txt")
