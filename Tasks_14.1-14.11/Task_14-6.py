def length_of_list(ls, length=0):
    if ls:
        return length_of_list(ls[1:], length + 1)
    return length

ls = ["Hello", "World", 1, 2, 3, 4, 5]

length = length_of_list(ls)

print(f"Length of list {ls} : {length} ")
