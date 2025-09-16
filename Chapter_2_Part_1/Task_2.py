# Cho chuỗi biểu diễn địa chỉ email:   "minhnhutvh@gmail.com"
# Rút trích và hiển thị chuỗi "gmail.com" (Đây chính là  tên Host)

data = "nguyent.22ns@vku.udn.vn"

position = data.find("@") # Tìm vị trí của ký tự "@"

username = data[:position] # Lấy phần trước @
domain = data[position + 1:] # Lấy phần sau @

print("Username:", username)
print("Domain:", domain)