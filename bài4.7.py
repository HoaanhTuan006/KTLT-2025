s = input("Nhập chuỗi: ")
kq = ""
for ch in s:
    if not ch.isdigit():
        kq += ch
print("Chuỗi sau khi loại bỏ số:", kq)
