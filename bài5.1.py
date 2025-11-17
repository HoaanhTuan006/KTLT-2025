
# ---- Phần module mymath ----
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    total = 0.0
    for v in values:
        total += v
    return float(total) / nvals

# ---- Phần sử dụng các hàm ----
values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(square(v))

print('Cubes:')
for v in values:
    print(cube(v))

print('Average:', average(values))

# Dùng "alias" (mô phỏng import as)
mt = __import__(__name__)  # tạm gán chính file này làm module
print(mt.square(2))
print(mt.square(3))
