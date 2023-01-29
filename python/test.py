a = [1,2,4]
A = [x for x in a if x > 0]
A = sorted(A)
for i in range(0, len(A) -1): # range 0,1 
    # print(i)
    # c = A
    # print(c)
    # print(A[i])
    # print(A[i+1])
    print(A[i+1] - A[i])
    # print(A[i+1])


