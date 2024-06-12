def my_bit_length(num):
    if num == 0:
        return 1

    length = 0

    while number > 0:
        length += 1
        num >>= 1

    return length

number = 10

print(my_bit_length(number))


