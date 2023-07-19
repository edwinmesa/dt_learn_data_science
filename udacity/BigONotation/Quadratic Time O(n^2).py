# Cuando realiza iteraciones anidadas, lo que significa tener un bucle en un bucle,
# la complejidad del tiempo es cuadrática, lo cual es horrible.

# Una manera perfecta de explicar esto sería si tiene una matriz con n elementos.
# El bucle exterior se ejecutará n veces, y el bucle interior se ejecutará n veces para 
# cada iteración del bucle exterior, lo que dará un total de n ^ 2 impresiones. 
# Si la matriz tiene diez elementos, diez imprimirán 100 veces (10^2).

def bubble_sort(arr):
    n = len(arr)                    #1 n = 5
    for i in range(n - 1):          #1   = [0,1,2,3,None]
        for j in range(n - i - 1):  #1   = j - (5 - 0 - 1) == 4
                                   
            if arr[j] > arr[j + 1]: #1   = 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #Init  = [5, 3, 8, 2, 1]
                                                        #1     = [3, 5, 8, 2, 1]
    return arr

# Example usage
arr = [5, 3, 8, 2, 1]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 5, 8]