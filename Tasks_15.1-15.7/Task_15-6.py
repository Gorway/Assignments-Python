def fibonacci(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fibonacci_numbers = [1, 1]

    current = 1
    prev = 1
    next_num = 0

    for i in range(2, n):
        next_num = current + prev
        fibonacci_numbers.append(next_num)
        prev, current = current, next_num

    return fibonacci_numbers

user_input = int(input("Enter number to see a list of Fibonacci numbers up to the entered number: "))

result = fibonacci(user_input)

print(result)

