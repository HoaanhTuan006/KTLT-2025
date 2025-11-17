

# --- Phần module (hàm xử lý) ---
def find_max_min(lst):
    """Trả về phần tử nhỏ nhất và lớn nhất trong danh sách"""
    lst_sorted = sorted(lst)       # Sắp xếp danh sách tăng dần
    smallest = lst_sorted[0]
    largest = lst_sorted[-1]
    return smallest, largest

# --- Phần chương trình chính ---
n = int(input("Nhập số lượng phần tử trong list: "))
lst = []

for i in range(n):
    value = int(input(f"Nhập giá trị thứ {i+1}: "))
    lst.append(value)

# Gọi hàm đã định nghĩa ở trên
smallest, largest = find_max_min(lst)

print("Danh sách đã nhập:", lst)
print("Phần tử nhỏ nhất:", smallest)
print("Phần tử lớn nhất:", largest)
