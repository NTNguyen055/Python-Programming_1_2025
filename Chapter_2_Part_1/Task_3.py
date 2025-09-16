# Cho chuỗi biểu diễn địa chỉ email và thời gian:   "

data = "nguyent.22ns@vku.udn.vn Wed August 27 1:16:10"

start_position = data.find("@") # Tìm vị trí của ký tự "@"

end_position = data.find(" ", start_position) # Tìm vị trí của ký tự khoảng trắng sau "@"

host = data[start_position + 1 : end_position] # Chỉ lấy phần sau ký tự @ và trước khoảng trắng

print("Domain:", host)
