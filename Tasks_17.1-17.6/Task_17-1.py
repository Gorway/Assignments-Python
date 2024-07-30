#Built-in map() function custom implementation

def custom_map(function: callable, *iterables: list) -> list:
    """
    Parameters:
    function: A function that takes one or more arguments and returns a value.
    *iterables: One or more iterables to apply the function to.

    Returns:
    List: A list of results where each result is the output of the function applied to
    corresponding elements of the input iterables.

    Example:
    - custom_map(lambda x: x * 10, [1, 2, 3]) returns [10, 20, 30]
    - custom_map(min, [1, 2, 3, 10], [4, 5, 6, 7]) returns [1, 2, 3, 7]
    
    """
    # Determine the minimum length of all iterables
    min_length = min(len(it) for it in iterables)
    
    result = []
    
    for i in range(min_length):
        # Gather the i-th element from each iterable
        items = [it[i] for it in iterables]
        
        # Apply the function to the gathered items and append the result
        result.append(function(*items))
    
    return result

numbers = [1, 2, 3]
result = custom_map(lambda x: x * 10, numbers)
print(f"Numbers {numbers} multiplied by 10 --> {result}.") 

list1 = [12, 24, 32, 120]
list2 = [44, 52, 61, 272, 1233]
result = custom_map(min, list1, list2)
print(f"Min values of 2 lists of numbers {list1} and {list2} --> {result}.") 

