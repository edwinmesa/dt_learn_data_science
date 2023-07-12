# this code was generate by chatgpt
import sys

def binary_search(arr, target):
    low  = 0
    high = len(arr) - 1 # 9 pos

    while low <= high:
        mid = (low + high) // 2 
                                #1  (9//2)    = 4
                                #2  (5+9)//2  = 7
                                #3  (5+6)//2  = 5
        print(mid)
        if arr[mid] == target:  #1 10 == 12 : No - Next
                                #2 16 == 12 : No - Next
                                #3 12 == 12 : Si - End
            return mid
        elif arr[mid] < target: #1 10 < 12  : Si - In
                                #2 16 < 12  : No - Next
            low = mid + 1       #1 4 + 1    : Regresa
        else:
            high = mid - 1      # 7 - 1     : Next
    
    return -1

# Example usage
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target  = 12

result  = binary_search(numbers, target) 
if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found")
print('*' * 60)
#************************************************************************#    
# sys.exit(0)

def binary_search_text(arr, target):
    """This function performs a case-insensitive search for the given `target` string in array"""
    low   = 0
    hight = len(arr) - 1

    while low <= hight:
        middle = (low + hight) // 2
        if   arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle + 1
        else:
            hight = middle - 1
    return -1

# Example usage
names        = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
target_name  = 'Eve'

res     = binary_search_text(names, target_name)

if result != -1:
    print(f"Found {target_name} at index {res}")
else:
    print(f"{target_name} not found")