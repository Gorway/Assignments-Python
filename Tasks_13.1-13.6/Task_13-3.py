def print_list_elems(ls):
    if len(ls) == 0:
        print("List is empty.")
    else:
        print("List elements: ")
        for element in ls:
            print(element)

size = 5
ls = []

for i in range(size):
    user_input = input("Enter list element: ")
    ls.append(user_input)

print_list_elems(ls)
