matrix = [[1,2,3,4], [5,6,7,8,8] , [12,23,31,123]]

for row in matrix:
    print(row)

max_element = matrix[0][0]

for row in matrix:
    for element in row:
        if element > max_element:
            max_element = element

print(max_element)


