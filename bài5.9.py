
def binary_search(lst, value):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False

# --- Chương trình chính ---
lst = sorted(list(map(int, input("Nhập danh sách (đã hoặc sẽ được sắp xếp): ").split())))
value = int(input("Nhập giá trị cần tìm: "))

found = binary_search(lst, value)

print("Danh sách:", lst)
if found:
    print(f"✅ Giá trị {value} có trong danh sách.")
else:
    print(f"❌ Giá trị {value} không có trong danh sách.")
