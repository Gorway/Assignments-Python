matrix_size = int(input("Enter matrix size: "))

matrix = []

print(f"Enter matrix elements {matrix_size}x{matrix_size}: ")

for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        element  = int(input(f"Element [{i}][{j}]: "))
        row.append(element)
    matrix.append(row)


print("Matrix:")
for row in matrix:
    print(row)
