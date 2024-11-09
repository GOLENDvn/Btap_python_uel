n=int(input("Nhập N: "))
tong = 0
for i in range (1,n):
    tong += i+(0.1*(i+1))
print(f"tổng là {tong}")