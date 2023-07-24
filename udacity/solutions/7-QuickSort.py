"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
from random import randint
def quicksort(array):
    if len(array) < 2:
        return array
    
    low, same, high = [],[],[]
    pivot = array[randint(0, len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    
    return quicksort(low) + same + quicksort(high)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))