size = 3

matrix = [[x + y for x in range(size)] for y in range(1, 10, 3)]

transposed = []

for i in range(size):
    row = []
    for j in range(size):
        row.append(matrix[j][i])
    transposed.append(row)

del matrix

for row in transposed:
    print(row)


"""    Columns Index
          00 01 02
          10 11 12
          20 21 22
"""
