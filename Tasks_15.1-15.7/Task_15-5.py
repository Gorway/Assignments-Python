def find_max(num1, num2, num3):
    max_num = num1

    numbers = (num1,num2,num3)

    for i in range(1,len(numbers)):
        if max_num < numbers[i]:
            max_num = numbers[i]

    return max_num


numbers = input("Enter three number, separated by spaces: ")

num1, num2, num3 = map(int, numbers.split())

max_number = find_max(num1,num2,num3)

print(f"Max number is: {max_number}")
