from math import sqrt
def phuongtrinh2():
    a=float(input("nhập hệ số a: "))
    b=float(input("nhập hệ số b: "))
    c=float(input("nhập hệ số c: "))
    if a==0:#bx+c=0
        if b==0 and c==0:
            print("Vô số nghiệm")
        elif b==0 and c!=0:
            print("Vô nghiệm")
        else:
            print("x="-c/b)
    else:
        delta=b**2-4*a*c
        if delta<0:
            print("Vô nghiệm")
        elif delta==0:
            print("Nghiệm kép x1 = x2 = "-b/(2*a))
        else:
            x1 = (-b - sqrt(delta))/(2*a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            print(f"x1 = {x1} ;x2 = {x2}")
while True:
    a = input("Có muốn giải phương trình bậc 2 không? y/n: ")
    if a == "y":
        phuongtrinh2()
    elif a == "n":
        break
    else:
        print("Không hợp lệ mời nhập lại!")
