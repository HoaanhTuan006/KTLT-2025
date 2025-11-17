
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i  # tìm thấy tại vị trí i
    return False, -1  # không tìm thấy

# --- Chương trình chính ---
dlist = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
item = int(input("Nhập giá trị cần tìm: "))

found, pos = Sequential_Search(dlist, item)

if found:
    print(f"✅ Tìm thấy {item} tại vị trí {pos}")
else:
    print(f"❌ Không tìm thấy {item} trong danh sách")
