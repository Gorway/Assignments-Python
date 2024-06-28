# Task 8-1

ls = [1, 2, 3, 5]

insert_index = 3

insert_data = 4

for i in range(len(ls)):
    if i == insert_index:
        ls.append(ls[i])
        ls[-1] == ls[i]
        ls[i] = insert_data
print(ls)


#ls = ls[:insert_index] + [insert_data] + ls[insert_index:]

#print(ls)


