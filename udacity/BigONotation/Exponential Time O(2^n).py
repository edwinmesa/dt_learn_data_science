# Se obtiene una complejidad de tiempo exponencial cuando la tasa de crecimiento 
# se duplica con cada adición a la entrada (n), a menudo iterando a través de todos 
# los subconjuntos de los elementos de entrada. Cada vez que una unidad de entrada aumenta en 1,
# el número de operaciones ejecutadas se duplica.

# La secuencia recursiva de Fibonacci es un buen ejemplo. 
# Supongamos que se le da un número y desea encontrar el enésimo
# elemento de la secuencia de Fibonacci.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fib = fibonacci(6)
print(fib)
