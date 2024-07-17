def length_of_list(ls, length=0):
    if length == len(ls):
        return length
    return length_of_list(ls, length + 1)

ls = ["Hello", "World", 1, 2, 3, 4, 5]

length = length_of_list(ls)

print(f"Length of list {ls} : {length} ")
