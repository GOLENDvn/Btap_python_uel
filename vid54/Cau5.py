k=int(input("nhập lãi suất (đơn vị %): "))
x=int(input("nhập số tiền gửi: "))
n=int(input("nhập số tháng gửi: "))

for i in range (1,n+1):
    x+=k*(x/100)
print(f"sau khi gửi {n} tháng số tiền bạn nhận được là {x}")