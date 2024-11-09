p=int(input("nhập số tiền mua trả góp: "))
x=int(input("nhập số tiền kiếm được: "))
r=int(input("nhập lãi suất kiếm được (đơn vị %): "))
t=0
while x <= p:
    t+=1
    x+=x*(r/100)
print(f"cần {t} tháng để trả góp {p}")