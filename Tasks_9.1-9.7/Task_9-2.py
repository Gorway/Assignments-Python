array = []

max_size = 5

max_index = 0
min_index = 0

while len(array) < max_size:
    input_int = int(input("Enter number: "))

    array.append(input_int)

for i in range(1, max_size):
    if array[i] > array[max_index]:
        max_index = i
    if array[i] < array[min_index]:
        min_index = i

index_difference = max_index - min_index

#making positive num from negative
#index_difference = -index_difference if index_difference < 0 else index_difference

print(f"The index differenc between max and min element is {index_difference}.")

