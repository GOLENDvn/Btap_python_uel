
def hinhvuong1 (n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print("")
def hinhvuong2 (n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==(n-1) or j==(n-1):
                print("*",end="")
            else:
                print(" ",end="")
        print("")
def tamgiac1(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
def tamgiac2 (n):
    for i in range(n):
        for j in range(n):
            if i==j or j==0 or i==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
def tamgiac3 (n):
    for i in range(n):
        for j in range(n):
            if i <= j:
                print("*",end="")
            else:
                print(" ",end="")
        print("")
def tamgiac4(n):
    for i in range(n):
        for j in range(n):
            if i==(n-1-j) or j==0 or i==0:
                print("*",end="")
            else:
                print(" ",end="")
        print("")


