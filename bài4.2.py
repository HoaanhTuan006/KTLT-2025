S = input("Nhập chuỗi: ")
for ch in S:
    if ch not in [' ', '\t']:  # bỏ qua khoảng trắng và tab
        print(ch)
