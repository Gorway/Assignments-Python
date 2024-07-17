def sum_of_digits(num):
    if num <= 0:
        return 0
    return  (num % 10) + sum_of_digits(num // 10)

num = 1243

result = sum_of_digits(num)

print(f"Sum of digits number ({num}) = {result}.")
