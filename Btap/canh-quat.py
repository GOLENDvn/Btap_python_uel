h=int(input("Nhập chiều cao: "))
for i in range((h-1),-h,-1):
    for j in range(-(h-1),h):
        if i==-j or -i==j or i==0 or (j==-(h-1) and i>0 ) or (j==h-1 and i<0):
            print("*",end="")
        else:
            print(" ",end="")
        if j == h - 1:
            print()