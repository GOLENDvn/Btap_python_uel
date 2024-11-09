tong=0
n=-1
while n < 0:
    n=int(input("Nhập n: "))
    tong += n
    if n < 0:
        print("số âm!")
        print("-"*30)
print(f"tổng các số nhập vào là {tong}")