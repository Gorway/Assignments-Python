def sum_of_elements(ls):
    if not ls:
        return 0

    return ls[0] + sum_of_elements(ls[1:])


ls = [1, 2, 3, 4, 5]

result = sum_of_elements(ls)

print(f"Sum of list {ls} elemets = {result}.")
