# this code was generate by chatgpt
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # recursive call : 5*4*3*2*1 = 120

# testing the factorial
n = 5
print("Factorial of", n, "is:", factorial(n))

# sys.exit(0)
print('*' * 60)
#************************************************************************#

def fibonacci(n):
    if n <= 1: # base case: Fibonacci of 0 is 0, Fibonacci of 1 is 1
        return n
    else: # The Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones
          # 
        return fibonacci(n - 1) + fibonacci(n - 2) # recursive call 1+2=3,2+3=5,3+5=8,5+8=13,8+13=21....
    
# Testing the fibonacci function
n2 = 8
print("Fibonacci of", n2, "is: ", fibonacci(n2))

# sys.exit(0)
print('*' * 60)
#************************************************************************#

def power(base, exponent):
    if exponent == 0: # base case: any number raised to the power of 0 is 1
        return 1
    else:
        return base * power(base, exponent - 1) # recursive call : 3*3*3*3=81

base = 3
exp  = 4
res  = power(base, exp)

print(f"{base} raised to power of {exp} is {res}")

# sys.exit(0)
print('*' * 60)
#************************************************************************#

def sum_list(numbers):
    if len(numbers) == 0:  # base case: an empty list has a sum of 0
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:]) # recursive call 1+2+3+4+5+6: 21
    
nums  = [1,2,3,4,5,6]
res2  = sum_list(nums)
print(f"The sum of the list {nums}: is {res2}")

# sys.exit(0)
print('*' * 60)
#************************************************************************#

def binary_search(arr, target, low, high):
    if low > high:
        # Base Case : element not found in array. Return -1
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Element Found at index 'mid'
            return mid
        elif arr[mid] > target: #1 5 > 8 : Si - NO - NEXT
            # recursive call on the left half
            return binary_search(arr, target, low, mid - 1)
        else:
            # recursive call on the right half
            return binary_search(arr, target, mid + 1, high)
# Testing the binary_search function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target  = 8
res3    = binary_search(numbers, target, 0, len(numbers) - 1)

if res3 != -1:
    print(f"Target {target} found at index {res3}")
else:
    print(f"Target {target} not found in the list")