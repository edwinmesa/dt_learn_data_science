# this code was generate by chatgpt
# Memoization Decorator

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result     = func(*args, **kwargs)
        end_time   = time.time()
        print(f"Execution Time: {end_time - start_time} seconds.")
        return result
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@time_decorator
@memoize
# decorator to apply the function with caching mechanism
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = fibonacci(10)
print("result fibonacci with decorator", result)

print('*' * 60)
#************************************************************************#

def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError('Input must be an integer')
        return func(*args, **kwargs)
    return wrapper

@validate_input
def multiply(a,b):
    return a * b

result = multiply(3,4)
print("result multiply", result)

# this line error
# result = multiply(3,"4")

print('*' * 60)
#************************************************************************#
# Retry Decorator:
import random
import time

def retry_decorator(max_attemps, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attemps:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Retry attemp {attempts} due to error: {str(e)}")
                    time.sleep(delay)
            raise Exception("Maximum retry attemps reached")
        return wrapper
    return decorator        

@retry_decorator(max_attemps=3)

def perform_operation():
    if random.randint(1, 10) <= 5:
        raise Exception("Ramdom error ocurred")
    else:
        return "Operation successful"

result = perform_operation()
print(result)

print('*' * 60)
#************************************************************************#

def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class DatabaseConnection:
    def __init__(self, url):
        self.url = url

db1 = DatabaseConnection("https://example.com/db")
db2 = DatabaseConnection("https://example.com/db")

print(db1 is db2)

print('*' * 60)
#************************************************************************#
# Deprecated Decorator:
import warnings

def deprecated(func):
    def wrapper(*args, **kwargs):
        warnings.warn(f"Function {func.__name__} is deprecated", DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper

@deprecated
def old_function():
    print("This is and old function")

old_function()

print('*' * 60)
#************************************************************************#
# Authentication Decorator
def authenticate(username, password):
    if username == "admin" and password == "secret":
        return True
    else:
        return False

def authentication_required(func):
    def wrapper(*args, **kwargs):
        if authenticate(username, password):
            return func(*args, **kwargs)
        else:
            raise Exception('Authentication failed')
    return wrapper

# @authentication_required
def restricted_function():
    print("This function requieres authentication")

restricted_function()

print('*' * 60)
#************************************************************************#
# Caching Decorator
def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


@time_decorator
@cache_result
def expensive_operation(x,y):
    # expensive computation
    return x + y

result  = expensive_operation(3,4)
print("result1", result)

result2 = expensive_operation(3,4)
print("result2", result2)
