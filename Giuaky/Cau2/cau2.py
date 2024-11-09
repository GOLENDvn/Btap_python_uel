h=int(input("nhập vào chiều cao h: "))
if h%2==0:
    h2=h//2
else:
    h2=h//2+1
for i in range(1,h+1):
    if i <= h2:
        print(" "*((h2-i)*2),end="")
        print(i,end="")
        if i == 1:
            print(end="")
        elif i == 2:
            print(" "*3,end="")
            print(i,end="")
        else:
            print(" "*(3+(i-2)*4),end="")
            print(i, end="")
        print(" "*((h2-i)*4-1),end="")
        if i == 1:
            print(i)
        elif i==h2:
            print(" "*(3+(i-2)*4),end="")
            print(i)
        else:
            print(" "*(((h2-i)-1)*2-2),end="")
            print(i,end="")
            print(" " * (3 + (i - 2) * 4), end="")
            print(i)
    else:
        i=h2-(i-h2)
        print(" " * ((h2 - i) * 2), end="")
        print(i, end="")
        if i == 1:
            print(end="")
        elif i == 2:
            print(" " * 3, end="")
            print(i, end="")
        else:
            print(" " * (3 + (i - 2) * 4), end="")
            print(i, end="")
        print(" " * ((h2 - i) * 4 - 1), end="")
        if i == 1:
            print(i)
        elif i == h2:
            print(" " * (3 + (i - 2) * 4), end="")
            print(i)
        else:
            print(" " * (((h2 - i) - 1) * 2 - 1), end="")
            print(i, end="")
            print(" " * (3 + (i - 2) * 4), end="")
            print(i)

