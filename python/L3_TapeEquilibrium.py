# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# import random
# import unittest

def solution(A):
    # Implement your solution here
    # pass
    sum_of_left = 0
    sum_of_right = sum(A)
    # print(sum_of_left, sum_of_right)

    best = None

    for P in range(0, len(A) - 1):
        sum_of_left  +=  A[P]
        sum_of_right -=  A[P]
        # print(sum_of_left, sum_of_right)
        diference = abs(sum_of_left-sum_of_right)
        # print(diference)
        best = diference if best is None or diference < best else best
    return best    

A = [3,1,2,4,3]

print(solution(A))