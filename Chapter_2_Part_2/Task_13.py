# Viết một chương trình cho phép người dung nhập vào một chuỗi trên nhiều dòng,
# sau đó chuyển các dòng này thành chữ in hoa và in ra màn hình. Yêu cầu:

lines = []

while True:

    line = input("Nhập vào một dòng (hoặc nhập 'DONE' để kết thúc): ")

    if line == 'DONE': break 

    lines.append(line.upper())

print("\n".join(lines))