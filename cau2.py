def donghocat (n):
    for i in range(n):
        for j in range(n):
            if i <= n//2:
                if i==0 or i <= j <= (n-1-i) :
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if i==(n-1) or (j<=i and j >= (n-1-i)):
                    print("*", end="")
                else:
                    print(" ", end="")
        print("")
while True:
    n=int(input("Nhập n: "))
    if n <= 0:
        print("nhập lại đi: ")
    else:
        donghocat(2*n-1)
        break