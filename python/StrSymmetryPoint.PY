
def solution(S):
    if len(S)%2 == 0:
        return -1
    mid = len(S)//2
    start = 0
    end = -1
    while start < mid:
        if S[start] != S[end]:
            return -1
        start += 1 
        end -= 1
    print(mid)
    return mid

solution('racecar')    