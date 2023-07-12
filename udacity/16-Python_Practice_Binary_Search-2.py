# this code was generate by chatgpt
def binary_search_rotated(arr, target):
    low  = 0
    high = len(arr) -1

    while low <= high:  #1 0 <= 7
                        #2 4 <= 7
        mid = (low + high) // 2 #1 (0+7)//2 = 3
                                #2 (4+7)//2 = 5 
        if arr[mid] == target:  #1 2 == 4: No - Next
                                #2 4 == 4: Si - End
            return mid
        
        # check left side of the array for rotation point
        if arr[low] <= arr[mid]: # 8 <= 2 : No - Next
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low  =  mid + 1
        
        # check left side of the array for ratation point
        else:
            if arr[mid] < target <= arr[high]: #  2 < 4 <= 6
                low  = mid + 1                 #1 4
            else:
                high = mid - 1
    return -1

# Example usage
numbers = [8, 9, 10, 2, 3, 4, 5, 6]
target_number = 4
result = binary_search_rotated(numbers, target_number)
if result != -1:
    print(f"Found {target_number} at index {result}")
else:
    print(f"{target_number} not found")

print('*' * 60)
#************************************************************************#    