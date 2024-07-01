arr = [1, 2, 3, 4, 5]
arr2 = [1, 2, 2, 4, 5]

equal = True

for i in range(len(arr)):
    if arr[i] != arr2[i]:
        equal = False
        break

if equal:
    print(f"Arrays {arr} and {arr2} are equal.")
else:
    print(f"Arrays {arr} and {arr2} are not equal.")

