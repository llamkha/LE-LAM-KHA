# Ma trận 2 chiều (3x3) cho ví dụ
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Tính tổng của tất cả các phần tử trong ma trận
total_sum = sum(sum(row) for row in matrix)

print(f"Tổng của các phần tử trong ma trận là: {total_sum}")

