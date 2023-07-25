# this code was generate by chatgpt
import hashlib
import os

def hash_string(s):
    # Create a hashlib object for MD5 hashing
    hash_object = hashlib.md5()
    # Update the hashlib object with the string
    hash_object.update(s.encode())
    # Get the hexadecimal representation of the hash
    hashed_string = hash_object.hexdigest()

    return hashed_string

# Example usage
input_string = "Hello, world!"
hashed_string = hash_string(input_string)

print("Hashed string:", hashed_string)

print('*' * 60)
#************************************************************************#
# Hashing Passwords (with Salt):

def hash_password(password, salt=None):
    # Generate a random salt if not provided
    if not salt:
        salt = os.urandom(16)
    # Create a hashlib object for SHA256 hashing
    hash_object = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    # Get the hexadecimal representation of the hash and salt
    hashed_password = hash_object.hex()
    salt = salt.hex()

    return hashed_password, salt

# example usage

password = "SecretPassword123"
hashed_password, salt = hash_password(password)
print("Hashed Password:", hashed_password)
print("Salt:", salt)