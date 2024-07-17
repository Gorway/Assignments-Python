def ascending_order(n):
    if n > 1:
        ascending_order(n - 1)
    print(n, end='')

n = 5

ascending_order(n)
print()
