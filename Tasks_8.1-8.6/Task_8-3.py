# Task 8-3

ls = [1, 2, 3, 4, 5]

last_element = 0

if len(ls) > 0:
    for i in ls:
        if ls[i] == ls[-1]:
            last_element = ls[i]
            del ls[-1]
            break
else:
    print("List is empty.")

print(f"Last element is {last_element}.")
print(f"List after pop(): {ls}")

