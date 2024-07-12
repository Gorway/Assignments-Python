def find_max_min(ls):

    max = ls[0]
    min = ls[0]

    for num in ls:
        if num > max:
            max = num
        elif num < min:
            min = num

    return max, min

ls = [112, 232, 331, 4123, 5123, 64, 712, 812, 912, 140]

max , min = find_max_min(ls)

print(f"Max element: {max}, Min element: {min}")
