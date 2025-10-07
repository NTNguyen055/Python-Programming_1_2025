from Dict import *

max = int(input("Nhập 1 số nguyên dương: "))

d = Dict_Create(max)

print("In các phần tử trong từ điển")
Print_Item(d)

print("In số thứ tự của các phần tử từ điển")
Print_Key(d)

print("In các giá trị của các phần tử từ điển")
Print_Value(d)