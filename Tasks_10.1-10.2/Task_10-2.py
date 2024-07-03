size = 4

matrix = [[(x + y * size + 1) for x in range(size)] for y in range(size)]

reversed_matrix = [[matrix[size - 1 - i][size - 1 - j] for j in range(size)] for i in range(size)]

print("Original Matrix")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

print("Reversed Matrix")
for row in reversed_matrix:
    for element in row:
        print(element, end=' ')
    print()
