# Esto es similar a la complejidad del tiempo lineal, excepto que el tiempo de ejecución 
# no depende del tamaño de entrada, sino de la mitad del tamaño de entrada. 
# Cuando el tamaño de entrada disminuye en cada iteración o paso, se dice que un 
# algoritmo tiene complejidad de tiempo logarítmica.

# Este método es el segundo mejor porque su programa se ejecuta para la mitad del
# tamaño de entrada en lugar del tamaño completo. Después de todo, el tamaño de entrada disminuye con cada iteración.

def complex_something(items):
    
    for i in range(5):
        print("python is awesome")
    
    for item in items:
        print(item)

    for item in items:
        print(item)

    print("Big O")
    print("Big O")
    print("Big O")    

complex_something([4,5,6,8])

# O(5) + O(n) + O(n) + O(3)
# O(8) + O(2n) = O(8+2n)

print('*' * 60)
#************************************************************************# 

def binary_search(arr, target):
    low  = 0
    high = len(arr) - 1

    while low <= high:
        mid   = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: # search the right half of array
            low  = mid + 1
        else:
            high = mid -1       # decrease left to find the target
    
    return -1

# Example usage
arr     = [2, 4, 6, 8, 10, 12, 14, 16]
target  = 10

index = binary_search(arr, target)
print(index)