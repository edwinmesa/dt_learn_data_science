# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is 
# surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: 
# one of length 4 and one of length 3. The number 20 has binary representation
#  10100 and contains one binary gap of length 1. The number 15 has binary 
# representation 1111 and has no binary gaps. The number 32 has binary representation 
# 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. 
# The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5,
#  because N has binary representation 10000010001 and so its longest binary gap is of length 5. 
# Given N = 32 the function should return 0, 
# because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].

import unittest
import re as regex

def solution(N):
    # Implement your solution here
    # pass
    N_binary = "{0:b}".format(N)
    gaps = regex.split("1+", N_binary)
    max_gap = []
    repetitions = len(gaps) -1
    for i in range(0, repetitions):
        max_gap.append(len(gaps[i]))
        print(max_gap)
    return max(max_gap)    

# solution(1041)

class TestMethods(unittest.TestCase):
    def test_Local1(self):
        n = 1041
        val = solution(n)
        self.assertEqual(val, 5)
    
    def test_Local2(self):
        n = 32
        val = solution(n)
        self.assertEqual(val, 0)
    
    def test_Local3(self):
        n = 15
        val = solution(n)
        self.assertEqual(val, 0)

if __name__ == '__main__':
    unittest.main()
