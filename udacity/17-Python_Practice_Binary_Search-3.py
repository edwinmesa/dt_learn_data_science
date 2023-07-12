# this code was generate by chatgpt
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
def binary_search_objects(arr, target):
    low  = 0
    high = len(arr) -1

    while low <= high:
        mid   = (low + high)//2

        if arr[mid].age == target.age:
            return mid
        elif arr[mid] < target.age:
            low = mid + 1
        else:
            high= mid - 1
    return -1

# Example usage
people = [
    Person('Alice', 25),
    Person('Bob', 30),
    Person('Charlie', 35),
    Person('David', 40),
    Person('Eve', 45),
]

target_person = Person('Charlie', 35)
result        = binary_search_objects(people, target_person)

if result != -1:
    print(f"Found {target_person.name} at index {result}")
else:
    print(f"{target_person.name} not found")