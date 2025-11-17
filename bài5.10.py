def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist

# --- Chương trình chính ---
nlist = list(map(int, input("Nhập danh sách cần sắp xếp: ").split()))
print("Danh sách ban đầu:", nlist)
sorted_list = bubbleSort(nlist)
print("Danh sách sau khi sắp xếp:", sorted_list)
