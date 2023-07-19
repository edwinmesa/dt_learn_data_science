# Se obtiene complejidad de tiempo lineal cuando el tiempo de 
# ejecución de un algoritmo aumenta linealmente con el tamaño de la entrada.
# Esto significa que cuando una función tiene una iteración que itera sobre un 
# tamaño de entrada de n, se dice que tiene una complejidad temporal de orden O(n).

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))

print('*' * 60)
#************************************************************************# 

def linear_something(items):
    for item in items:
        print(item)

linear_something([4,5,6,8])