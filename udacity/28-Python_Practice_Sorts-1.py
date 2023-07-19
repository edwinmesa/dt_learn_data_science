# this code was generate by chatgpt
def bubble_sort(our_list):
    for i in range(len(our_list)): #idx: 0=19,1=13,2=6,3=2,4=18,5=8
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) -1): #idx: i,j = 0,0 - 0,1- 0,2 - 0,3 - 0-4 .....
            # print(our_list[j], "-", our_list[j+1])
            if  our_list[j] > our_list[j+1]: # 19>13, 13>6, 6>2, 2>18, 18>8
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                # print(our_list[j],"-",our_list[j+1], "=", our_list[j+1],"-",our_list[j])
    return our_list

our_list = [19, 13, 6, 2, 18, 8]
b        = bubble_sort(our_list)
print(b)