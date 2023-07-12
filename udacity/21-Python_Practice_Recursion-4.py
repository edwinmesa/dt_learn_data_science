# this code was generate by chatgpt

# GCD (Greatest Common Divisor):
# The greatest common divisor (GCD) of two numbers is the largest number
# that divides both of them without leaving a remainder.
# Here's a recursive function to calculate the GCD using Euclid's algorithm:

def gcd(a,b):
    if b == 0:
        return abs(a) # base case for recursion termination
    else:
        return gcd(b, a % b)

# testing the gcd function
num1 = 12
num2 = 15
result = gcd(num1, num2)
print(f"the GCD of {num1} and {num2} is {result}")

print('*' * 60)
#************************************************************************#

def reverse_string(string):
    if len(string) <= 1:
        return string # base case: empty string or single character
    else:
        return reverse_string(string[1:]) + string[0]  # recursive call to reverse substring

word   = "hello"
result = reverse_string(word)

print(f"The reversed string of '{word}' is '{result}'")