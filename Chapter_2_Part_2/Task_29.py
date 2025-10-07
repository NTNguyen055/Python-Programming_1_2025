# Viết chương trình đọc độ dài ba cạnh của một tam giác từ người dùng. Sau đó hiển thị một thông báo cho biết loại tam giác

def type_of_triangle (ab, bc, ac):

    if ab + bc > ac and ab + ac > bc and ac + bc > ab: 

        if (ab == bc == ac):
            print(f"Đây là tam giác đều! Có cạnh: ab = bc = ac = {ab}")
        
        elif ab == ac or ab == bc or bc == ac:
            if ab == ac:
                print(f"Đây là tam giác cân có cạnh ab = ac = {ab}")

            elif ab == bc:
                print(f"Đây là tam giác cân có cạnh ab = bc = {ab}")

            else:
                print(f"Đây là tam giác cân có cạnh bc = ac = {bc}" )
        else:
            print(f"Đây là tam giác thường có ab = {ab}, bc = {bc} và ac = {ac}")
    
    else:
        print("Vui lòng nhập lại ba cạnh tam giác sao cho hợp lệ!")

ab = float(input("Nhập độ dài cạnh ab của 1 tam giác: "))
bc = float(input("Nhập độ dài cạnh bc của 1 tam giác: "))
ac = float(input("Nhập độ dài cạnh ac của 1 tam giác: "))

type_of_triangle(ab, bc, ac)


    

