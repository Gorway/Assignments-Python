def my_bit_count(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

number = 16

print(my_bit_count(16))
