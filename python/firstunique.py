def solution(A):
    counts = {}
    for item in A:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in A:
        if counts[item] == 1:
            return item
    return -1

print(solution([1,2,1,3,2,5])) # prints 3

print(solution([4,10,5,4,2,10])) # prints 5
