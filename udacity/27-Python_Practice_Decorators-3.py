# this code was generate by chatgpt
import time

def rated_limited(max_calls, time_period):
    def decorator(func):
        calls = []
        def wrapper(*args, **kwargs):
            current_time = time.time()
            calls.append(current_time)
            call_within_period = [t for t in calls if t >= current_time - time_period]
            if len(call_within_period) > max_calls:
                wait_time = time_period - (current_time - call_within_period[0])
                time.sleep(wait_time)

            return func(*args, **kwargs)
        return wrapper
    return decorator


@rated_limited(max_calls=3, time_period=5)
def limited_function():
    print("This function is has rate limiting")

limited_function()
limited_function()
limited_function()
limited_function()

print('*' * 60)
#************************************************************************#
# Type Checking Decorator

def type_check(arg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, arg_types[i]):
                    raise TypeError(f'Argument {i+1} should be of type {arg_types[i].__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@type_check([int, str])
def process_data(num, name):
    print(f"Processing data: {num}, {name}")

process_data(10, "Edwin")   
# process_data("10", "Edwin")   # error


print('*' * 60)
#************************************************************************#
# Debugging Decorator
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

import time

@debug
def calculate(a, b):
    result = a * b
    return result

calculate(2,4)

print('*' * 60)
#************************************************************************#
# Context Manager Decorator:
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    yield
    end_time   = time.time()
    print(f"Elapsed time: {end_time - start_time} seconds")

with timer():
    time.sleep(4)