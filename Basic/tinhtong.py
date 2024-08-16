n = int(input("Nhập giá trị n: "))
i = 1
s = 0
while i <= 2 * n + 1:
    s += i
    i += 2

print(f"Tổng của chuỗi 1 + 3 + 5 + ... + (2n+1) với n = {n} là: {s}")