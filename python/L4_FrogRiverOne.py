# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import unittest

def solution(X, A):
    # Implement your solution here
    # pass
    leaves = set()

    for count, leaf in enumerate(A):
        # print(leaf)

        if leaf <= X:
            leaves.add(leaf)
            # print("--- leaves",leaves)
            if len(leaves) >= X:
                # print("--- len", len(leaves))
                # print("--- count", count)
                # print(count -1)
                return count
                
    return -1

# X = 5
# A = [1, 3, 1, 4, 2, 3, 5, 4]

# solution(X, A)

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)

if __name__ == '__main__':
    unittest.main()