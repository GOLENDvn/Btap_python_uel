n=int(input("nhập n: "))
i=n
giaithua=1
while i > 1:
    giaithua *= i
    i-=1
print(f"{n}! = {giaithua}")