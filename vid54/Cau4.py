n=int(input("nhập N: "))
giaithua=1
for i in range (n,1,-1):
    giaithua *= i
print(f"{n}! = {giaithua}")