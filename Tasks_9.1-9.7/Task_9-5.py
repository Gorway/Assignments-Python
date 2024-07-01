matrix = [ [1,2,3], [4,5,6], [7,8,9] ]

sum_of_main_diagonal = 0

size = len(matrix)

for i in range(size):
    sum_of_main_diagonal += matrix[i][i]


print(f"Sum of main diagonal elements: {sum_of_main_diagonal}.")
