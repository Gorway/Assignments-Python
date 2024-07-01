matrix = [ [1,2,3] , [4,5,6], [7,8,9] ]

size = len(matrix)

# Main diagonal
 # for i in range(size):
  # print(matrix[i][i])

# Secondary diagonal
 # for i in range(size):
  # print(matrix[i][size-1-i])

for i in range(size):
    matrix[i][i] , matrix[i][size-1-i] = matrix[i][size-1-i], matrix[i][i]

print("Matrix after swaping main and secondary diagonals: ")
for row in matrix:
    print(row)
