# explanation big o Notation
import numpy as np

given_array = np.random.randint(1,1000, 1000)
# given_array = [1,2,3,4,5,6,7,8,9,10]

def find_sum(given_array):
    total = 0
    for i in given_array:
        total += 1
    return total

print(find_sum(given_array))
