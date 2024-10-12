def bubble_sort(arr):
  size = len(arr)
  for i in range(size - 1):
    already_swapped = False
    for j in range(size - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j+1], arr[j]
        already_swapped = True
    if not already_swapped:
      break

arr = [10, 65, 255, 4, 78, 988, 1, 22]
bubble_sort(arr)
print(arr)