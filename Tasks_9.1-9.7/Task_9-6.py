matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

sum_of_secondary_diagonal = 0

size = len(matrix)

for i in range(size):
    sum_of_secondary_diagonal += matrix[i][size-1-i]


print(f"Sum of secondary diagonal elements: {sum_of_secondary_diagonal}.")
