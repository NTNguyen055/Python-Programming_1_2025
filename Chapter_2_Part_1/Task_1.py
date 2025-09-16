# Viết chương trình nhập vào một chuỗi
# Xuất ra màn hình chuỗi ký tự hoa
# Xuất ra màn hình chuỗi ký tự có ký tự đầu là ký tự hoa
# Xuất ra màn hình chuỗi ký tự thường

st = input("Enter your string:") # yêu cầu nhập chuỗi

st_upper = st.upper() #Viết hoa
st_title = st.title() #Viết hoa chữ cái đầu
st_lower = st.lower() #Viết thường

print("Uppercase:", st_upper)
print("Lowercase:", st_lower)
print("Titlecase:", st_title)
