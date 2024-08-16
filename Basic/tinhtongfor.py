n = int(input("Nhập giá trị n: "))
total = 0
for i in range(1, n + 1):
    total += i**i

print(f"Tổng của chuỗi 1 + 2^2 + 3^3 + ... + n^n với n = {n} là: {total}")
