"""
1. In the given C file, the strategy used to grow arrays when full is implemented in the list_resize function.
   
new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
This line of the code calculates the new allocated size of the list and the growth factor can be approximated to be 1.125
because newsize + (newsize >> 3) adds newsize/8 to newsize, increasing the size by 12.5%. +6 ensures that the list 
has some minimum growth even for small lists and &~(size_t)3 rounds the size down to the nearest multiple of 4. Therefore, 
this strategy ensures that the list grows by approximately 12.5% each time it needs to expand

"""

import timeit
import sys
import matplotlib.pyplot as plt

def lst_grow_test():
    lst = []
    S = 0
    last_size = sys.getsizeof(lst)
    for i in range(64):
        lst.append(i)
        current_size = sys.getsizeof(lst)
        if current_size != last_size:
            print(f"Growth at {len(lst)} element: {last_size} bytes to {current_size} bytes")
            S = i
            last_size = current_size

    return S

S = lst_grow_test()

def growth_time(S, iter=1000):
    return timeit.repeat(
        stmt="lst.append(0)",  
        setup=f"lst = [0] * {S}",  
        repeat=5,  
        number=iter
    )


time_1 = growth_time(S)
time_2 = growth_time(S-1)


plt.figure(figsize=(10,10))
plt.hist(time_1, bins=30, alpha=0.5, label=f"S to S+1")
plt.hist(time_2, bins=30, alpha=0.5, label=f"S-1 to S")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.legend()
plt.title("Timing Distribution for List Growth")
plt.savefig("ex3.jpg")

"""
5. The timing distribution for growing from S to S+1 is higher and more spread out as compared 
to growing from S-1 to S because growing from S to S+1 involves memory reallocation.

"""