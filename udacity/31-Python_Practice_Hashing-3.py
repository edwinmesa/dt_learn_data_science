class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        # Initialize an empty list (buckets) to store key-value pairs
        self.capacity = capacity
        self.size = 0  # Keep track of the number of elements
        self.table = [None] * self.capacity

    def _hash_function(self, key):
        # Simple hash function to map keys to an index within the capacity
        return hash(key) % self.capacity

    def insert(self, key, value):
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
                    # If the key already exists, update the value and return
                    current.value = value
                    return
                current = current.next
            # Add a new node at the end of the linked list
            current.next = Node(key, value)

        self.size += 1
        # Check if it's time to resize the hashtable
        if self.size >= self.capacity * 0.7:
            self._resize()

    def _resize(self):
        # Double the capacity and rehash all elements
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity

        for bucket in self.table:
            current = bucket
            while current:
                index = hash(current.key) % new_capacity
                if new_table[index] is None:
                    new_table[index] = Node(current.key, current.value)
                else:
                    # Handle collision using chaining (linked list)
                    new_current = new_table[index]
                    while new_current.next:
                        new_current = new_current.next
                    new_current.next = Node(current.key, current.value)
                current = current.next

        self.table = new_table
        self.capacity = new_capacity

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
        # Use the key as the hash to find the index of the bucket
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
                self.size -= 1
                return
            prev = current
            current = current.next

    def keys(self):
        # Return a list of all keys in the hashtable
        keys_list = []
        for bucket in self.table:
            current = bucket
            while current:
                keys_list.append(current.key)
                current = current.next
        return keys_list

    def values(self):
        # Return a list of all values in the hashtable
        values_list = []
        for bucket in self.table:
            current = bucket
            while current:
                values_list.append(current.value)
                current = current.next
        return values_list

    def load_factor(self):
        # Calculate the load factor (number of elements / capacity)
        return self.size / self.capacity

    def clear(self):
        # Clear all key-value pairs from the hashtable
        self.capacity = 10
        self.size = 0
        self.table = [None] * self.capacity

# Example usage
hash_table = HashTable()

# Insert key-value pairs into the hashtable
hash_table.insert("apple", 3)
hash_table.insert("banana", 6)
hash_table.insert("orange", 2)
hash_table.insert("apple", 5)  # Updating the value for an existing key

# Calculate and display the load factor
print("Load Factor:", hash_table.load_factor())

# Check key existence
# print("Does 'apple' exist?", hash_table.contains_key("apple"))  # True
# print("Does 'grape' exist?", hash_table.contains_key("grape"))  # False

# Retrieve values using keys
print("Value of 'apple':", hash_table.get("apple"))
print("Value of 'banana':", hash_table.get("banana"))

# Get all keys and values
print("All keys:", hash_table.keys())
print("All values:", hash_table.values())

# Get the size of the hashtable
# print("Size of the hashtable:", hash_table.size())

# Remove a key-value pair
hash_table.remove("orange")

# Try to retrieve the value for the removed key
print("Value of 'orange' after removal:", hash_table.get("orange"))

# Clear the hashtable
hash_table.clear()

# Get the size after clearing
# print("Size of the hashtable after clearing:", hash_table.size())
