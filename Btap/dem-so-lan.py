chuoi = {}
s=input("nhập string: ")
for i in range(len(s)):
    if s[i] in chuoi:
        chuoi[s[i]]+=1
    else:
        chuoi[s[i]]=1
lis=[]
for j in range (3):
    max=0
    for i in range(len(s)):
        if chuoi[s[i]] > max and s[i] not in lis:
            max = i
    lis[j] = max
print(f"Ký tự {s[lis[1]]} xuất hiện {chuoi[s[lis[1]]]} lần, {s[lis[2]]} xuất hiện {chuoi[s[lis[2]]]} lần, {s[lis[3]]} xuất hiện {chuoi[s[lis[3]]]} lần")

