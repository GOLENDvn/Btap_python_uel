n=int(input("Nhập n: "))
tong = 0
for i in range (0,n*2+1,2):
    tong += i
print(f'tổng {n} số chẵn đầu tiên là {tong}')

