# Store functions for common list transformations (e.g., sorting, reversing, filtering, mapping) in a dictionary. Write a function transform_list(lst, operation) that uses this dictionary to perform the requested transformation on a list.
def mapList(lst, func):
    return [func(x) for x in lst]

def sortList(lst):
    return sorted(lst)

def reverseLlist(lst):
    return list(reversed(lst))

def filterList(lst, condition):
    return [x for x in lst if condition(x)]

def isEven(n):
    return n % 2 == 0

list_operations = {
    'sort': sortList,
    'reverse': reverseLlist,
    'filter': filterList,
    'map': mapList
}

def transform_list(lst, operation, *args):
    if operation in list_operations:
        return list_operations[operation](lst, *args)
    else:
        raise ValueError(f"Unsupported operation: '{operation}'")
    
example_list = [ 1,2,11,2,3,4,9,8,7,6,5]
result = transform_list(example_list, 'filter', isEven)
print(result)