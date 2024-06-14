n = int(input("Enter matix size: "))

matrix = []

print("Enter matrix elements: ")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Element[{i}][{j}]: "))
        row.append(element)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    for element in row:
        print(element)


