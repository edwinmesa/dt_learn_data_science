# this code was generate by chatgpt
import os

def get_directory_size(dir):
    total_size = 0
    for item in os.scandir(dir):
        if item.is_file():
            total_size += item.stat().st_size
        elif item.is_dir():
            total_size += get_directory_size(item.path)
    return total_size

# Testing the get_directory_size function
directory_path = '/home/pydev/workflow/dt_learn_data_science/udacity'
result         = get_directory_size(directory_path)

print(f"the total size of {directory_path} and its subdirectories is {result} bytes")
print('*' * 60)
#************************************************************************#
def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        # move disk from source peg to auxiliary peg using destination as a buffer
        tower_of_hanoi(n - 1, source, auxiliary, destination )
        print(f"Move disk {n} from {source} to {destination}")
        tower_of_hanoi(n - 1, auxiliary, destination, source)

# Testing the tower_of_hanoi function
num_disks = 3
tower_of_hanoi(num_disks,'A','C', 'B')
print('*' * 60)
#************************************************************************#

def permutations(string):
    if len(string) == 1:
        return [string]
    else:
        perms = [] # list to store permutations
        for i in range(len(string)):
            # Extract the current character
            char = string[i]
            # Generate permutations of the remaining characters
            remainig_chars = string[:i] + string[i+1:]
            subperms       = permutations(remainig_chars)
            # Append the current character to each permutation of the remaining characters
            for subperm in subperms:
                perms.append(char + subperm)
    return perms    

# Testing the permutations function
word   = "abc"
result = permutations(word)
print(f"The permutations of '{word}' are:")
for perm in result:
    print(perm)

print('*' * 60)
#************************************************************************#

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
number = 12345
result = sum_of_digits(number)
print(f"the sum of digits in {number} is {result}")
