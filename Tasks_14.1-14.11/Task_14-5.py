def print_list_elements(num_list, start=0):
    if start >= len(num_list):
        return
    print(num_list[start], end=' ')
    print_list_elements(num_list, start + 1)

num_list = [1, 2, 3, 4, 5]

print("List elements: ", end=' ')
print_list_elements(num_list)
print()
