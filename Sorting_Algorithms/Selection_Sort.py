def selection_sort(arr):
  size = len(arr)
  
  for i in range(size):
    min_ind = i
  
    for j in range(i + 1, size):
      if arr[j] < arr[min_ind]:
        min_ind = j
    
    if min_ind != i:
      arr[i], arr[min_ind] = arr[min_ind], arr[i]
      

arr = [10, 50, 11, 54, 487, 78, 8, 1, 6, 77]
selection_sort(arr)
print(arr)