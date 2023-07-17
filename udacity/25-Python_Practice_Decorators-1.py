# this code was generate by chatgpt
# Logging Decorator:
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function: ", func.__name__)  # logging the name of called functions.
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

res = add(3,5)
print("result:",res)

print('*' * 60)
#************************************************************************#

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result     = func(*args, **kwargs)
        end_time   = time.time()
        print(f"Execution Time: {end_time - start_time} seconds.")
        return result
    return wrapper

@time_decorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(7)
print("result factorial", result)


print('*' * 60)
#************************************************************************#

def authorize_decorator(allowed_roles):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                raise Exception("Unauthorized Access")
        return wrapper
    return decorator

user_role = "admin"
# or any other role from the list of authorized roles
@authorize_decorator(["admin", "superadmin"])
def delete_file(file_path):
    print(f"Deleting file: {file_path}")
# test the result is ok
delete_file("/path/to/file.txt")
# test the result is an exeption
user_role = "guest"
delete_file("/path/to/file.txt")