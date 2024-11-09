from math import sqrt
n=int(input("nhập n: "))
print("các ước của n: ",end="")
for i in range (1,int(sqrt(n))+1):
    if i < sqrt(n):
        if n % i == 0:
            print(i,end=" ")
            print(int(n/i),end=" ")
    else:
        print(i,end=" ")
