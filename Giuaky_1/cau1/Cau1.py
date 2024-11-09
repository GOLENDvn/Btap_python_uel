price_carrot = 10000
price_cabbage = 8000
price_potato = 12000
price_onion = 9000
price_pumpkin = 11000

total_revenue = 3630000

total_weight = int(input('nhập tổng khối lượng bán được: '))

for hanh in range(0, total_weight + 1):  # Số kg cà rốt
    carot = hanh * 2  # Số kg hành tây
    for khoai in range(0, total_weight + 1):  # Số kg khoai tây
        bcai = carot + khoai - 15  # Số kg bắp cải
        bdo = total_weight - (carot + bcai + khoai + hanh)  # Số kg bí đỏ
        # Tính tổng tiền thu được
        tong_tien = (carot * price_carrot + bcai * price_cabbage + khoai * price_potato + hanh * price_onion + bdo * price_pumpkin)
        if tong_tien == total_revenue and (carot>=0 or bcai>=0 or khoai>=0 or hanh>=0 or bdo >=0):
                print(f"Cà rốt: {carot} kg, Bắp cải: {bcai} kg, Khoai tây: {khoai} kg, Hành tây: {hanh} kg, Bí đỏ: {bdo} kg")

