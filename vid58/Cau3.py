from math import sqrt
def snt (n):
    global tong
    a=0
    for i in range (2,int(sqrt(n))+1):
        if n % i == 0:
            break
        else:
            a=1
    if a == 1:
        return(n)
    else:
        return(0)
n=int(input("nhập n: "))
tong = 0
for i in range (1,n+1):
    tong += snt(i)
print(f"tổng các số nguyên tố từ 1 đến {n} là {tong}!")

