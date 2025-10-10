# Thực hiện chương trình đếm số từ trong nhiều file text

from pathlib import Path

def count_words(filename):
    try:
        file_path = Path(__file__).parent / filename
        contents = file_path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print(f"File '{filename}' không tồn tại trong thư mục: {file_path.parent}")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"File '{filename}' có {num_words} từ.")

filenames = ['ntn1.txt', 'ntn2.txt', 'ntn3.txt']

for filename in filenames:
    count_words(filename)
