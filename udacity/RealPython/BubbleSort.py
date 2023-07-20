from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

ARRAY_LENGTH = 10000

if __name__ == "__main__":
    array = [randint(0,1000) for i in range(ARRAY_LENGTH)]
    # Run sorting algorithms on the same input data and compare execution speeds.
    run_sorting_algorithm(algorithm="sorted", array=array)

print('*' * 60)
#************************************************************************#

def bubble_sort(array):
    n = len(array)

    for i in range(n):                              #idx: 0=19,1=13,2=6,3=2,4=18,5=8
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):                  #idx: i,j = 0,0 - 0,1- 0,2 - 0,3 - 0-4 .....
            if array[j] > array[j + 1]:             # 19>13, 13>6, 6>2, 2>18, 18>8
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j] 

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False
        
        if already_sorted:
            break
    
    return array

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="bubble_sort", array=array)