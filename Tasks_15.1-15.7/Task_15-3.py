def is_ascending_order(ls):
    if len(ls) <= 1:
        return True

    if ls[0] > ls[1]:
        return False

    return is_ascending_order(ls[1:])

ls = [1, 3, 2, 5, 4]

if is_ascending_order(ls):
    print(f"List {ls} is sorted in ascending order.")
else:
    print(f"List {ls} is not sorted in ascending oreder.")


