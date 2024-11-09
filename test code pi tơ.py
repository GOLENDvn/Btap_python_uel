h=int(input("nhập h: "))
#khởi tạo bảng có h hàng và 2h-1 cột
#trong đó giá trị các phần tử là -1
matrix = [[-1 for _ in range(2*h-1)] for _ in range(h)]

#thiết lập hình chữ V bằng số 1
for i in range (h):
    for j in range (2*h-1):
        if i == j or i + j == 8:
            matrix [i][j] = 1

#tạo các số trong tam giác ngược
for i in range (h-2,-1,-1):
    for j in range (1,2*h-2):
        matrix[i][j]=matrix[i+1][j-1]+matrix[i+1][j+1]+1

#các giá trị bằng 0 hoặc -1 thì gán thành space
#các giá trị khác thì in ra giá trị
for i in range (h):
    for j in range (2*h-1):
        if matrix [i][j] == 0 or matrix [i][j]==-1:
            print(" ",end="")
        else:
            print(matrix [i][j],end="")
    print()
