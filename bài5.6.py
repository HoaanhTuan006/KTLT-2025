
n = int(input("Nhập số lượng phần tử trong list: "))
lst = []

for i in range(n):
    value = int(input(f"Nhập giá trị thứ {i+1}: "))
    lst.append(value)

# Tìm giá trị nhỏ nhất, lớn nhất
min_val = min(lst)
max_val = max(lst)

# Tìm vị trí (index)
min_index = lst.index(min_val)
max_index = lst.index(max_val)

print("Danh sách đã nhập:", lst)
print("Giá trị nhỏ nhất:", min_val, "ở vị trí:", min_index)
print("Giá trị lớn nhất:", max_val, "ở vị trí:", max_index)
