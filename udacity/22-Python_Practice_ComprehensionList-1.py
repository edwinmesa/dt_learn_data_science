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

list1                   = [1, 2, 3, 4]
list2                   = [5, 6, 7, 8]
combined_list_10        = [(x, y) for x in list1 for y in list2 if x + y > 10]
combined_normal         = [(x,y) for x in list1 for y in list2]
print("Combine Lists if x + y and greater than 10: ", combined_list_10)
print("Combine Lists normal: ", combined_normal)
print('*' * 60)
#************************************************************************#
# Generating a matrix using nested list comprehensions:
matrix   = [[row * col for col in range(1,6)] for row in range(1,6)]
print("matriz_1: ", matrix)
matrix_2 = [[row + col for row in range(1,5)] for col in range(1,5)]
print("matriz_2: ", matrix_2)
matrix_3 = [[row - col for row in range(1,4)] for col in range(1,4)]
print("matriz_3: ", matrix_3)
print('*' * 60)
#************************************************************************#
# Extracting unique characters from a list of strings:
words          = ["hello", "world", "open", "ai"]
unique_chars_1 = list({char for word in words for char in word})
print("unique_words_1:", unique_chars_1)
words_2        = ["kilo","we","mar","uv"]
unique_chars_2 = list({char for word in words_2 for char in word})
print("unique_words_2:", unique_chars_2)

print('*' * 60)
#************************************************************************#
# Generating a list of prime numbers:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

limit           = 20
limit_2         = 45
prime_numbers_1 = [x for x in range(2, limit)   if is_prime(x)]
prime_numbers_2 = [x for x in range(2, limit_2) if is_prime(x)]
print("limit_1:", prime_numbers_1)
print("limit_2:", prime_numbers_2)

print('*' * 60)
#************************************************************************#