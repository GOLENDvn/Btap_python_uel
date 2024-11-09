luong=int(input("nhập lương trung bình hằng tháng (triệu đồng): "))

if luong < 10 :
    print("Loại tiêu chuẩn!")
elif luong < 20:
    print("Loại bạc!")
elif luong < 50:
    print("Loại vàng!")
else:
    print("Khách VIP!")
