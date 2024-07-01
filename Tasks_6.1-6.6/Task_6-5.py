array = [4,6,5,2,1,7,10,9,8,3]

index = 0

size = len(array)

for i in range(size):
    if array[i] % 2 == 0:
        array[i], array[index] = array[index], array[i]
        index += 1

array[:index] = sorted(array[:index])
array[index:] = sorted(array[index:])

print(f"Array: {array}")
