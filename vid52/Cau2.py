def tinh_thue () :
    thuesuat=float((input("nhập thuế suất (đơn vị %): ")))
    thuesuat/=100
    giatinh=int(input("nhập giá tính thuế (nghìn vnđ): "))
    print(f"giá thuế là: {round(thuesuat*giatinh,2)} nghìn vnđ")

while True:
    a=input("Có muốn tính thuế không? y/n: ")
    if a == "y":
        tinh_thue()
    elif a == "n":
        break
    else:
        print("Không hợp lệ mời nhập lại!")

