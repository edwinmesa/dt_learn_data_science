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
# Finding common elements between two lists:
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
list3 = [3,6,7,8,9]
list4 = [7,9,6,5,1]
common_elements = [x for x in list1 if x in list2]
print("common elements",common_elements)
non_common_elements = [x for x in list1 if x not in list2 ]
print("non_common elements",non_common_elements)

print('*' * 60)
#************************************************************************#
# Creating a dictionary from two lists:
keys    = ['a', 'b','c','d']
values  = [1,2,3]
keys2   = ["green","red","blue"]
values2 = [100,300,405] 
dictionary  = {k:v for k,v in zip(keys, values)}
print("dict_1:", dictionary)
dictionary2 = {k:v for k,v in zip(keys2, values2)}
print("dict_2:", dictionary2)

print('*' * 60)
#************************************************************************#
# Finding the sum of squares of even numbers and cubes of odd numbers:
numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [4,6,7,8,9]
result   = sum([num ** 2 if num % 2 == 0 else num ** 3 for num in numbers])
result2  = sum([num ** 2 if num % 2 == 0 else num ** 3 for num in numbers2 ])
print("sum_odd_even", result)
print("sum_odd_even_2", result2)

print('*' * 60)
#************************************************************************#
# Extracting vowels from a string ignoring case:
string   = "Hello, World!"
vowels   = [char for char in string if char.lower() in 'aeiou']
string2  = "message"
no_vowel = [char for char in string2 if char.lower() not in 'aeiou']
print('Vowel characters:', (vowels))
print('No Vowel characters:', (no_vowel))

print('*' * 60)
#************************************************************************#
# Finding all anagrams in a list of words:
words     = ['cat', 'dog', 'tac', 'god', 'act']
words2    = ["pol","lop","edw","plo","dre","pli","der","red"] 
anagrams  = [word for word in words  if  sorted(word)  == sorted(words[0])]
anagrams2 = [word for word in words2 if  sorted(word)  == sorted(words2[0])]
print("anagrams_1", anagrams)
print("anagrams_2", anagrams2)

print('*' * 60)
#************************************************************************#
# Creating a matrix transpose using nested list comprehensions:
matrix    = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_2  = [[10,15,20],[25,30,40],[40,60,90],[90,35,58]]
traspose  = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
traspose2 = [[row[i] for row in matrix_2] for i in range(len(matrix_2[0]))]
print("traspose:", traspose) 
print("traspose2:", traspose2) 

print('*' * 60)
#************************************************************************#
# Extracting unique words from a list of sentences:
sentences      = ["I am learning", "learning is fun", "fun is important"]
sentences2     = ["I love Caroline is wonderfull", "the life is great", "python is great"]
unique_words   = list({word for sentence in sentences  for word in sentence.split()})
# set to remove duplicates then convert back into list
unique_words_2 = list({word for sentence in sentences2 for word in sentence.split()})
print("unique words", unique_words)
print("unique words2", unique_words_2)

print('*' * 60)
#************************************************************************#
# Calculating the average of each student's grades in a nested list:
grades   = [[80, 90, 95], [85, 95, 92], [70, 75, 80], [90, 92, 88]]
averages = [sum(student_grades) / len(student_grades) for student_grades in grades]
print("averages", averages)