# this code was generate by chatgpt
class HashTable:
    def __init__(self) -> None:
        # Initialize an empty dictionary to store key-value pairs
        self.table = {}
    
    def insert(self, key, value):
        """Insert a new (key, value) pair into the hash table."""
        self.table[key] = value
    
    def get(self, key):
        """Return the value associated with `key` in the hash table or raise KeyError if it doesn't exists"""
        return self.table.get(key)
    
    def remove(self, key):
        # Remove the key-value pair from the dictionary
        if key in self.table:
            del self.table[key]

# example usage
hash_table = HashTable()
# Insert key-value pairs into the hashtable
hash_table.insert("apple", 3)
hash_table.insert("banana", 6)
hash_table.insert("orange", 2)

# Retrieve values using keys
print("Value of 'apple':", hash_table.get("apple"))
print("Value of 'banana':", hash_table.get("banana"))
print("Value of 'grape' (not in hashtable):", hash_table.get("grape"))

# Remove a key-value pair
hash_table.remove("orange")

# Try to retrieve the value for the removed key
print("Value of 'orange' after removal:", hash_table.get("orange"))


print('*' * 60)
#************************************************************************#

class HashTable2:
    def __init__(self) -> None:
        # Initialize an empty dictionary to store key-value pairs
        self.table = {}
    
    def insert(self, key, value):
        """Insert a new (key, value) pair into the hash table."""
        self.table[key] = value
    
    def get(self, key):
        """Return the value associated with `key` in the hash table or raise KeyError if it doesn't exists """
        return self.table.get(key)
    
    def remove(self, key):
        # Remove the key-value pair from the dictionary
        if key in self.table:
            del self.table[key]
    
    def keys(self):
        '''Returns all the existing keys'''
        return [k for k in self.table.keys()]
    
    def values(self):
        '''Return all the corresponding values stored with each respective key.'''
        return [v for v in self.table.values()]
    
    def size(self):
        '''Return number of elements present inside the Hashtable object at any given time.'''
        return len(self.table)
    
    def clear(self):
        '''Clears out everything that is currently being held by this instance of the class i.e '''
        self.table.clear()

# example usage
hash_table_2 = HashTable2()

# insert key-value pairs into the hashtable
hash_table_2.insert("apple",  3)
hash_table_2.insert("banana", 6)
hash_table_2.insert("orange", 2)

# Retrieve values using keys
print("Value of 'apple':", hash_table_2.get("apple"))
print("Value of 'banana':", hash_table_2.get("banana"))
print("Value of 'grape' (not in hashtable):", hash_table_2.get("grape"))

# Remove a key-value pair
hash_table_2.remove("orange")

# Try to retrieve the value for the removed key
print("Value of orange after removal:", hash_table_2.get("orange"))

# Get all keys and values
print("All Keys:", hash_table_2.keys())
print("All Values:", hash_table_2.values())

# Get the size of the hashtable
print("Size of the hashtable:", hash_table_2.size())

# Clear the hashtable
hash_table_2.clear()

# Get the size after clearing
print("Size of the hashtable after clearing:", hash_table_2.size())

print('*' * 60)
#************************************************************************#

class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.next = None

class HashTable3:
    def __init__(self, capacity=10) -> None:
        # Initialize an empty list (buckets) to store key-value pairs
        self.capacity = capacity
        self.table    = [None] * self.capacity

    def _hash_function(self, key):
        # Simple hash function to map keys to an index within the capacity
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        """Insert or update a new node with given `key` and its corresponding `value`."""
        # Use the key as the hash to find the index of the bucket
        index = self._hash_function(key)
        # Check if the bucket is empty
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Handle collision using chaining (linked list)
            current = self.table[index]
            while current.next:
                if current.key == key:
                    # If the key already exists, update the value and return.
                    current.value = value
                    return
                current.next = current
            # Add a new node at the end of the linked list
            current.next = Node(key, value)

    def get(self, key):
        # Use the key as the hash to find the index of the bucket
        index = self._hash_function(key)
        # Traverse the linked list to find the key
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

        # If the key is not found, return None
        return None
    
    def remove(self, key):
        # use the key as the hash to find the index of the bucket
        index = self._hash_function(key)
        # Handle collision using chaining (linked list)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    # If the node to remove is the head of the linked list
                    self.table[index] = current.next
                else:
                    # If the node to remove is in the middle or at the end
                    prev.next = current.next
                return
            prev    = current
            current = current.next
    
    def keys(self):
        """Return all unique keys stored by this HashTable."""
        key_list = []
        for bucket in self.table:
            current = bucket
            while current:
                key_list.append(current.key)
                current = current.next
        return key_list
    
    def values(self):
        """ Return a list of all values in the hashtable"""
        value_list = []
        for bucket in self.table:
            current = bucket
            while current:
                value_list.append(current.value) 
                current = current.next
        return value_list

    def size(self):
        # Return the number of key-value pairs in the hashtable
        count = 0
        for bucket in self.table:
            current = bucket
            while current:
                count += 1
                current = current.next
        return count
    
    def clear(self):
        "Remove all items from hash table."
        self.table = [None] * self.capacity
    
    def contains_key(self, key):
        # Check if the key exists in the hashtable
        index   = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False
    

# Example usage
hash_table_3 = HashTable3()

# Insert key-value pairs into the hashtable
hash_table_3.insert("apple",  3)
hash_table_3.insert("banana", 6)
hash_table_3.insert("orange", 2)
hash_table_3.insert("apple",  5)

# Check key existence
print("Does 'apple' exist?", hash_table_3.contains_key("apple"))  # True
print("Does 'grape' exist?", hash_table_3.contains_key("grape"))  # False

# Retrieve values using keys
print("Value of 'apple':", hash_table_3.get("apple"))
print("Value of 'banana':", hash_table_3.get("banana"))

# Get all keys and values
print("All keys:", hash_table_3.keys())
print("All values:", hash_table_3.values())

# Get the size of the hashtable
print("Size of the hashtable:", hash_table_3.size())

# Remove a key-value pair
hash_table_3.remove("orange")

# Try to retrieve the value for the removed key
print("Value of 'orange' after removal:", hash_table.get("orange"))

# Get the size of the hashtable
print("Contains Key:", hash_table_3.contains_key("apple"))

# Clear the hashtable
hash_table_3.clear()

# Get the size after clearing
print("Size of the hashtable after clearing:", hash_table_3.size())

print('*' * 60)
#************************************************************************#

