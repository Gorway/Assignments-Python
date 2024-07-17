def descending_order(n):
    if n <= 0:
        return
    descending_order(n, end='')
    print_num(n - 1)


n = 5

descending_order(n)
print()
