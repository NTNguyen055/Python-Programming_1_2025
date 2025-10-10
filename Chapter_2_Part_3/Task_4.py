# Tệp nén là một loại lưu trữ chứa một hoặc nhiều tệp đã bị giảm kích thước.
# Nén tập tin trong các hệ điều hành hiện đại thường khá đơn giản. Viết chương trình nén và giải nén tệp bằng Python

import zipfile
import os

# === Hàm nén nhiều file hoặc cả thư mục ===
def compress_files(source_paths, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for path in source_paths:
            if os.path.isfile(path):
                # Trường hợp là file -> ghi trực tiếp
                zipf.write(path, os.path.basename(path))
                print(f"Đã thêm file: {path}")
            elif os.path.isdir(path):
                # Trường hợp là thư mục -> duyệt toàn bộ cây thư mục
                for foldername, subfolders, filenames in os.walk(path):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, os.path.dirname(path))
                        zipf.write(file_path, arcname)
                        print(f"Đã thêm file trong thư mục: {file_path}")
    print(f"Đã nén thành công thành tệp '{zip_name}'")

# === Hàm giải nén ===
def decompress_file(zip_name, extract_to='.'):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Đã giải nén '{zip_name}' vào thư mục '{extract_to}'")

# === Chương trình chính ===
def main():
    print("=== CHƯƠNG TRÌNH NÉN & GIẢI NÉN TỆP ===")
    choice = input("Bạn muốn (1) Nén tệp/thư mục hay (2) Giải nén tệp? Nhập 1 hoặc 2: ")

    if choice == '1':
        print("\nNhập các đường dẫn tệp hoặc thư mục cần nén (ngăn cách bằng dấu phẩy):")
        paths = input("→ ").split(',')
        paths = [p.strip() for p in paths if p.strip() != '']

        zip_name = input("Nhập tên file .zip muốn tạo (vd: mydata.zip): ").strip()
        compress_files(paths, zip_name)

    elif choice == '2':
        zip_name = input("Nhập tên file .zip cần giải nén: ").strip()
        extract_to = input("Nhập thư mục để giải nén (Enter = thư mục hiện tại): ").strip() or '.'
        decompress_file(zip_name, extract_to)

    else:
        print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
