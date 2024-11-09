p=int(input("nhập số tiền cần trả góp (nghìn vnđ): "))
t = 0
x=1000
#mặc định số tiềm kếm được là 1,000,000 vnđ
#lãi suất cố định là 15%
while x<p:
    x+=x*0.15
    t+=1
print(f"cần trả góp {t} tháng!")
