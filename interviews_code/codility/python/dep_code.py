# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # Implement your solution here
    # pass
    steps      = set([i for i in range(1, X + 1 )])
    frog_steps = set() # use for create a new collection  unique

    for index, leaf in enumerate(A):
        frog_steps.add(leaf)
        print(index)
        print(leaf)
        if frog_steps == steps:
            return index
    return -1

solution(5, [1, 3, 1, 4, 2, 3, 5, 4])