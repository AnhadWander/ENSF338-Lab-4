import timeit
import random
import matplotlib.pyplot as plt

def linear_search(arr, key):
    """
    Inefficient search implementation - Linear Search.
    Worst case complexity - O(n).
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i 
    return -1

def binary_search(arr, key):
    """
    Efficient search implementation - Binary Search.
    Worst case complexity - O(logn).
    """
    lft, rit = 0, len(arr) - 1
    while lft <= rit:
        mid = (lft + rit) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lft = mid + 1
        else:
            rit = mid - 1 
    return -1

arr_size = 1000
sort_arr = sorted(random.sample(range(1, 100000), arr_size))
key = random.choice(sort_arr)

measure = 100

lin_time = timeit.repeat(lambda: linear_search(sort_arr, key), repeat=measure, number=1)
bin_time = timeit.repeat(lambda: binary_search(sort_arr, key), repeat=measure, number=1)

plt.figure(figsize=(10,10))
plt.plot(range(measure), lin_time, label="Linear Search")
plt.plot(range(measure), bin_time, label="Binary Search")
plt.xlabel("Iteration")
plt.ylabel("Time (seconds)")
plt.title("Search Algorithm Performance Over Multiple Runs")
plt.legend()
plt.savefig("Peformance.jpeg")