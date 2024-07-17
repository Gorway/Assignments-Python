def sum_of_natural_numbers(n):
    if n == 1:
        return n
    return n + sum_of_natural_numbers(n - 1)

n = 5

print(sum_of_natural_numbers(n))
