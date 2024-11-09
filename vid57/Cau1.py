from math import sqrt
a=int(input("nhập A: "))
tong=0
for i in range (1,int(sqrt(a))+1):
    if i < sqrt(a):
        if a % i == 0:
            tong+=i+int(a/i)
    else:
        tong += i
print(f"tổng ước = {tong}")
