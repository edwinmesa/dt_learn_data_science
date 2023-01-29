# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # pass
    N = len(A)+1
    # print(N)
    res1 = (N * (N + 1))//2
    # print(res1)
    res2 = sum(A)
    # print(res2)

    missing_value = res1-res2
    # print(missing_value)
    return missing_value

A = [1, 2, 3, 4, 6]

solution(A)