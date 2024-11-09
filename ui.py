from draw_tamgiac import hinhvuong1, hinhvuong2, tamgiac1, tamgiac2, tamgiac3, tamgiac4

while True:
    n=int(input("nhập n: "))
    if n < 0:
        print("nhập n dương!")
    else:
        break
while True:
    a=int(input("""Muốn vẽ hình gì?
1)Hình vuông bình thường
2)Hình vuông rút ruột công trình
3)tam giác bình thường
4)tam giác bình thường bị rút ruột
5)tam giác tư duy ngược
6)tam giác tư duy ngược bị rút ruột
0)exit
Mời nhập: """))
    match a:
        case 1:
            hinhvuong1(n)
            pass
        case 2:
            hinhvuong2(n)
            pass
        case 3:
            tamgiac1(n)
            pass
        case 4:
            tamgiac2(n)
            pass
        case 5:
            tamgiac3(n)
            pass
        case 6:
            tamgiac4(n)
            pass
        case _:
            break
