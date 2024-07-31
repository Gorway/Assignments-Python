def make_multiplier_of(n):
    def multiplier(x):
        return n * x
    return multiplier

n = [11, 22, 33]

list_of_functions = []
#collecting 3 function with arguments from 'n' list
for value in n:
    list_of_functions.append(make_multiplier_of(value))

# print(list_of_functions)

results = []

#multiply the value in the list 'n' by 1,2,3 with
for i in range(len(list_of_functions)):
    function = list_of_functions[i]
    results.append(function(i + 1))

print(f"The result of multiplying the values ​​in the list {n} by 1,2,3, respectively: {results}.")