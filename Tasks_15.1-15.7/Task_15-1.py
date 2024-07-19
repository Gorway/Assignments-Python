def flatten_list(nested_list):
    if not nested_list:
        return []

    flattened = []

#   """ for item in nested_list:
#        if type(item) == int:
#            flattened.append(item)
#        else:
#            flattened.extend(flatten_list(item))
#
#    return flattened"""

    return [item for sublist in nested_list
            for item in (flatten_list(sublist) if type(sublist) == list else [sublist])]

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]

flattened = flatten_list(nested_list)

print(f"Result: {flattened}")
