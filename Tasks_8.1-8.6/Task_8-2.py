# Task 8-2

ls = [1, 2, 3, 4, 5, 3]

remove_data = 3

done = False

for i in ls:
    if ls[i] == remove_data:
        del ls[i]
        done = True
        break

if done:
    print(ls)
else:
    print("Element does not exist")
