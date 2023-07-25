# this code was generate by chatgpt

array = [8,2,6,4,5]
s     = sorted(array)
print("sorted:", s)

print('*' * 60)
#************************************************************************#



def bubble_sort(our_list):
    for i in range(len(our_list)): #idx: 0=19,1=13,2=6,3=2,4=18,5=8
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) -1): #idx: i,j = 0,0 - 0,1- 0,2 - 0,3 - 0-4 .....
            # print(our_list[j], "-", our_list[j+1])
            if  our_list[j] > our_list[j+1]: # 19>13, 13>6, 6>2, 2>18, 18>8
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                print(our_list[j],"-",our_list[j+1], "=", our_list[j+1],"-",our_list[j])
    return our_list

our_list = [19, 13, 6, 2, 18, 8]
b        = bubble_sort(our_list)
print(b)


print('*' * 60)
#************************************************************************#

# Bubble Sort:

def buble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# example usage
arr = [5,3,8,2,1]
sorted_array = buble_sort(arr)

print("sorted with bubble sort:", sorted_array)

print('*' * 60)
#************************************************************************#

# Quick Sort

from random import randint

def quickSort(arr):
    if len(arr) < 2:
        return arr
    low, same, high = [],[],[]
    pivot = arr[randint(0, len(arr) -1)]

    for item in arr:
        if   item <  pivot : low.append(item)
        elif item == pivot : same.append(item)
        elif item >  pivot : high.append(item)
    
    return quickSort(low) + same + quickSort(high)

arrQuickS = [87,55,3,58,44,5694,1] 
quicks    = quickSort(arrQuickS)
print("quickSort:", quicks)

print('*' * 60)
#************************************************************************#
# Insertion Sorting

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        # Move elements of arr[0..i-1], that are greater than the
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr
arrInsertion = [87,55,3,58,44,73,1,9]
insertionsort=insertion_sort(arrInsertion)
print('Insertionsort:', insertionsort)