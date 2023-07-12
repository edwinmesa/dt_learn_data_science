# this code was generate by chatgpt

# Flattening a nested list:
nested_list    = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [element for sublist in nested_list for element in sublist]
print(f"Flattened List:", flattened_list)
print('*' * 60)
#************************************************************************#

nested_list_2    = [[10,11,12],[13,14,15],[16,17,18],[19,20,21]]
flattened_list_2 = [el for sub in nested_list_2 for el in sub]
print(f"Flattened List:", flattened_list_2)
print('*' * 60)
#************************************************************************#

nested_list_3    = [['a','b','c'],['d','e','f']]
flattened_list_3 = [elm for sub in nested_list_3 for elm in sub]
print(f"Flattened List:", flattened_list_3)
print('*' * 60)
#************************************************************************#

#Filtering even numbers and calculating their squares:
numbers       = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [num ** 2 for num in numbers if num % 2 == 0]
print("squared even", squared_evens)
print('*' * 60)
#************************************************************************#

numbers            = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_odd_by_3   = [num ** 3 for num in numbers if num % 2 != 0]
print("squared odd by 3", squared_odd_by_3)
print('*' * 60)
#************************************************************************#

list1         = [1, 2, 3, 4]
list2         = [5, 6, 7, 8]
combined_list = 