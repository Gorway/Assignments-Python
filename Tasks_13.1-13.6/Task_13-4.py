def digits_sum(num):

    sum = 0

    while num != 0:
        sum += num  % 10
        num //= 10

    return sum

num = 1234
result = digits_sum(num)
print(result)
