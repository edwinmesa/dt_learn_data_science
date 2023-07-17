# this code was generate by chatgpt
# Finding the squares of numbers divisible by 3 within a range:
names          = ["Alice Smith", "Bob Johnson", "Charlie Brown", "David Davis"]
sorted_names   = sorted(names, key=lambda x : x.split()[-1])
sorted_names_2 = sorted(names, key=lambda x : x.split()[0])
print("sorted names by last name",sorted_names)
print("sorted names by first name",sorted_names_2)
print('*' * 60)
#************************************************************************#
# Example: Filtering Prime Numbers
import math

numbers       = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = list(filter(lambda x : all(x % i !=0 for i in range(2, int(math.sqrt(x))+1)), numbers))
print("prime numbers", prime_numbers)

print('*' * 60)
#************************************************************************#
# Example 1: Squaring Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_even_num = list(map(lambda x : x ** 2 if x % 2 == 0 else x, numbers))
squared_odd_num  = list(map(lambda x : x ** 2 if x % 2 != 0 else x, numbers))
print("squared even:", squared_even_num)
print("squared odd:", squared_odd_num)

print('*' * 60)
#************************************************************************#
# Example 2: Mapping a List of Strings to their Lengths
words     = ["apple", "banana", "cherry", "date", "elderberry"]
len_str   = list(map(lambda x : len(x), words))
len_str_m = list(map(lambda x : len(x) if len(x) > 5 else 0, words))
print("len words", len_str)
print("len words m", len_str_m)


print('*' * 60)
#************************************************************************#
# Manipulating a List of Dictionaries
people      = [{"name": "Alice", "age": 25, "gender": "F"},{"name": "Bob", "age": 30,"gender": "M"},{"name": "Charlie", "age": 20,"gender": "M"}]
update_age  = list(map(lambda person: {** person, "is_adult": person["age"] >= 18}, people))
gender_word = list(map(lambda gender: {** gender, "gender_word":gender["gender"]=="F"}, update_age))

print("update age", update_age )
print("update gender", gender_word )

print('*' * 60)
#************************************************************************#
# Filtering Odd Numbers
numbers      = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
odd_numbers  = list(filter(lambda x : x % 2 != 0, numbers))

print("even numbers", even_numbers)
print("odd_numbers", odd_numbers)

print('*' * 60)
#************************************************************************#
# Converting Celsius to Fahrenheit
celsius_temperatures    = [0, 10, 20, 30, 40]
fahrenheit_temperatures = list(map(lambda c: (c * 9/5)+32, celsius_temperatures))
print('Celsius Temperature:', fahrenheit_temperatures)

print('*' * 60)
#************************************************************************#
# Sorting a List of Tuples by the Second Element
scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
sorted_tuples = sorted(scores, key=lambda x : x[0])
print("sorted tuples", sorted_tuples)

print('*' * 60)
#************************************************************************#
# Computing the Sum of Squares
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum(map(lambda x : x**2, numbers))
print("sum of squares", sum_of_squares)

print('*' * 60)
#************************************************************************#
# Capitalizing the First Letter of Each Word
sentence = "this is a sentence"
capitalized_sentence = " ".join(map(lambda word: word.capitalize(), sentence.split()))
print("capitalized_sentence", capitalized_sentence)

print('*' * 60)
#************************************************************************#
names  = ["Alice", "Bob", "Charlie", "David", "Eve"]
letter = "C"

filtered_names = list(filter(lambda name: name.startswith(letter), names))
print("Filtered Names",filtered_names)

print('*' * 60)
#************************************************************************#
numbers = [10, 15, 7, 21]
binary_list = list(map(lambda x : bin(x)[2:], numbers))
print("convert binary", binary_list)

print('*' * 60)
#************************************************************************#
# Reversing a List of Strings
names = ["Alice", "Bob", "Charlie", "David"]
reversed_names = list(map(lambda x : x[::-1], names))
print("reversed_names", reversed_names)

print('*' * 60)
#************************************************************************#
# Combining Two Lists using a Lambda Function
numbers = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']

combined_list = list(map(lambda x, y : str(x) + y, numbers, letters))
print("combined lists", combined_list)

print('*' * 60)
#************************************************************************#
# Mapping a List of Dictionaries to a Specific Key
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

ages = list(map(lambda person: person["age"], people))
print("ages:", ages)

print('*' * 60)
#************************************************************************#
# Counting Vowels in a List of Words
words = ["apple", "banana", "cherry", "date"]
vowel_counts = list(map(lambda word: sum(1 for char in word if char.lower() in 'aeiou'), words))
vowel_a      = list(map(lambda word: sum(1 for char in word if char.lower() in 'a'), words))
print('Vowel counts:', vowel_counts)
print('Vowel a:', vowel_a)

print('*' * 60)
#************************************************************************#
# Formatting Names as Last Name, First Name
names = ["Alice Smith", "Bob Johnson", "Charlie Brown", "David Davis"]
formatted_names = list(map(lambda name: ', '.join(name.split()[::-1]),names))
print("formatted_names", formatted_names)

print('*' * 60)
#************************************************************************#
# Filtering Palindromic Words
words = ["level", "radar", "python", "madam", "kayak"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print("palindromes", palindromes)

print('*' * 60)
#************************************************************************#
# Calculating the Sum of Squares using Map and Reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_squares = reduce(lambda x, y : x + y, map(lambda x: x**2, numbers) )
print("sum squares", sum_of_squares)

print('*' * 60)
#************************************************************************#
#  Mapping Multiple Lists using Lambda
numbers = [1, 2, 3, 4, 5]
multipliers = [10, 20, 30, 40, 50]
result = list(map(lambda x, y: x * y, numbers, multipliers))