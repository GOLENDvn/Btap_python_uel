level = input("nhập vào giá trị level: ")
if level=="low":
    thongtin="rủi ro thấp"
elif level=="medium":
    thongtin="rủi ro trung bình"
elif level=="high":
    thongtin="rủi ro cao"
else:
    thongtin="rủi ro không xác định"
print(f"mức rủi ro đầu tư: {thongtin}")