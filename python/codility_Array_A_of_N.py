# This is a demo task.

# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


import unittest

# def solution(A):
#     # Implement your solution here
#     # pass
#     m = max(A)
#     if m<= 0:
#         return 1
#     value_smallest = set(e for e in range(1, m+2))-set(A)
#     return min(value_smallest)   

def solution(B):
    A = [x for x in B if x > 0] # remove negative numbers
    A = sorted(A)   # order
    if 1 not in A:
        return 1
    for i in range(0, len(A) -1): # range between 0 and len list
        if A[i+1] - A[i] > 1:     # 
            print(A[i])
            return A[i] + 1
    return max(A) + 1      

class TestSolutionA(unittest.TestCase):
    def test_case1(self):
        list = [1, 3, 6, 4, 1, 2]
        val  = solution(list)
        self.assertEqual(val, 5)

    def test_case2(self):
        list = [1, 2, 3]
        val  = solution(list)
        self.assertEqual(val, 4)
        
    def test_case3(self):
        list = [-1, -3]
        val  = solution(list)
        self.assertEqual(val, 1)

    def test_case4(self):
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        val  = solution(list)
        self.assertEqual(val, 11)    

if __name__ == '__main__':
    unittest.main()         