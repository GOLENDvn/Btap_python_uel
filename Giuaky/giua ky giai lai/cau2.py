h=int(input("nhập chiều cao h: "))
h2=1
if h % 2 == 0:#nếu h là số chẵn thì đổi thành số lẻ bé hơn 1 đơn vị
    h2 = h
    h -= 1
for i in range(h//2,-(h//2+1),-1):
    for j in range(-(2*(h-1)),2*(h-1)+1):
        if i==0 and j in (0,-(2*(h-1)),2*(h-1)):#in ra hàng ở giữa với hàng i = 0 và j là giá trị ở giữa hoặc biên
            print(f"{int(h/2+0.5)}",end="")
            if j == 2 * (h - 1):
                print("")
                if h2 % 2 == 0: #nếu h là chẵn thì in thêm 1 dòng ở giữa
                    print(f"{int(h/2+0.5)}",end="")
                    print(" "*(2*(h-1)-1),end="")
                    print(f"{int(h/2+0.5)}", end="")
                    print(" " * (2*(h-1)-1), end="")
                    print(f"{int(h / 2 + 0.5)}")
        elif j == 2*(h - 1):#nếu j đến cột cuối cùng thì xuống dòng
            print("")
        #in ra các đường chéo
        #chia làm 2 phần từ cột có số 1 bên trái đến bên phải vẽ hình chữ x
        #cột ngoài vùng 1-1 thì vẽ đường chéo theo hướng ngược lại
        elif ((j in range (-(h-1),h) and (abs(2*i) == abs(j))) and i!=0) or (abs(j) in range (h,2*(h-1)+1) and (abs(2*(h//2-abs(i))+h//2*2) == abs(j))) :
            print(f"{int(h/2+0.5)-abs(i)}",end="")
        else:#các trường hợp còn lại thì in space
            print(" ",end="")