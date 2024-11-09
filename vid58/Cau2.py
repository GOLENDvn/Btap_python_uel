from math import sqrt
a=int(input("nhập số thứ nhất: "))
b=int(input("nhập số thứ hai: "))
if a > b:
    a,b = b,a
tong=0
for i in range (1,a+1):
    if a % i == 0 and b % i == 0:
        tong+=i
if tong == a:
    print(f"số {a} bằng tổng ước chung {tong}!")
elif tong == b:
    print(f"số {b} bằng tổng ước chung {tong}!")
else:
    print("không có số nào bằng tổng ước chung!")