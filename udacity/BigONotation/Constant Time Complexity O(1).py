# Cuando su algoritmo no depende del tamaño de entrada n, se dice 
# que tiene una complejidad de tiempo constante con orden O(1). 
# Esto significa que el tiempo de ejecución siempre será el mismo, independientemente del tamaño de entrada.

# O(C)
# O(1)

def firstElement(arr):
    return arr[0] # 1 step

score = [12, 55, 67, 94, 22]
print(firstElement(score))

print('*' * 60)
#************************************************************************# 

def constant_something(arr):
    result = arr[0] * arr[0] # 1 step
    print(result)            # 2 step

constant_something(score)

print('*' * 60)
#************************************************************************# 

steps = []
def constant(n):
    return 1

for i in range(1,100):
    steps.append(constant(i))