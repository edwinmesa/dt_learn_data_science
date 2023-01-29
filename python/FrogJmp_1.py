# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import unittest

import math


def solution(X, Y, D):
    # Implement your solution here
    # pass
    num = Y - X
    den = D
    jump = math.ceil(num/den)
    return jump


X = 10
Y = 40
D = 25

print(solution(X, Y, D))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        X = 10
        Y = 85
        D = 30
        val = solution(X, Y, D)
        self.assertEqual(val, 3)

    def test_local2(self):
        X = 10
        Y = 40
        D = 25
        val = solution(X, Y, D)
        self.assertEqual(val, 2)    


if __name__ == '__main__':
    unittest.main()