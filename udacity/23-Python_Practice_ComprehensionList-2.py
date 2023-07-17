# this code was generate by chatgpt
# Finding the squares of numbers divisible by 3 within a range:
start = 1
end   = 10
squared_divisible_by_3 = [num ** 2 for num in range(start, end + 1) if num % 3 == 0]
squared_divisible_by_4 = [num ** 4 for num in range(start, end + 1) if num % 4 == 0]
print("squared_div_3", squared_divisible_by_3)
print("squared_div_4", squared_divisible_by_4)

print('*' * 60)
#************************************************************************#
# Creating a list of tuples representing coordinates:
x_values = [1, 2, 3]
y_values = [4, 5, 6]
coordinates = [(x, y) for x in x_values for y in y_values]
print("coordinates", coordinates)

print('*' * 60)
#************************************************************************#
# Filtering a list of words based on their lengths:
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'kiwi']
filtered_words = [word for word in words if len(word) < 6]
print("filtered words", filtered_words)