# Tệp nén là một loại lưu trữ chứa một hoặc nhiều tệp đã bị giảm kích thước. 
# Nén tập tin trong các hệ điều hành hiện đại thường khá đơn giản. Viết chương trình nén và giải nén tệp bằng Python

import zipfile
import os

def compress_file(file_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))
    print(f"Đã nén file {file_path} thành {zip_path}")


def decompress_file(zip_path, extract_dir):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_dir)
    print(f"Đã giải nén {zip_path} vào thư mục {extract_dir}")


def main():
    # Ví dụ file cần nén
    file_to_compress = "test.txt"
    zip_file = "archive.zip"
    extract_folder = "extracted_files"

    # Nén file
    compress_file(file_to_compress, zip_file)

    # Giải nén file
    decompress_file(zip_file, extract_folder)


if __name__ == "__main__":
    main()
