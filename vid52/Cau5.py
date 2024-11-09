def dang_ky ():
    print("Vui lòng đăng ký lần đầu!")
    global tendangnhap, matkhau, i
    tendangnhap=input("nhập tên đăng nhập: ")
    while True:
        matkhau=input("nhập mật khẩu: ")
        matkhau2=input("nhập lại mật khẩu: ")
        if matkhau2==matkhau:
            break
        else:
            print("Không trùng khớp vui lòng nhập lại!")
    i=1
    print("-"*30)
    return(tendangnhap,matkhau,i)
def dang_nhap ():
    global j
    while True:
        print("Vui lòng đăng nhập!")
        name = input("nhập tên đăng nhập: ")
        pas = input("nhập mật khẩu: ")
        if name == tendangnhap and pas == matkhau:
            print("đăng nhập thành công!")
            j=True
            return(j)
            break
        else:
            print("tài khoản hoặc mật khẩu sai!")
        print("-"*30)
i=0
while True:
    if i==0:
        tendangnhap,matkhau,i = dang_ky()
    else:
        j=dang_nhap()
        if j:
            break
