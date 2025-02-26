import time
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def middle(self, start, last):
        if start is None:
            return None
        if start == last:
            return start

        slow = start
        fast = start.next

        while fast != last:
            fast = fast.next
            slow = slow.next
            if fast != last:
                fast = fast.next

        return slow

    def binary_search(self, value):
        start = self.head
        last = None

        while True:
            mid = self.middle(start, last)

            if mid is None:
                return False

            if mid.data == value:
                return True

            elif start == last:
                break

            elif mid.data < value:
                start = mid.next

            elif mid.data > value:
                last = mid

        return False

class Array:
    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)
        self.data.sort()  

    def binary_search(self, target):
        left, right = 0, len(self.data) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.data[mid] == target:
                return True  
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False  

def measure_performance(structure, size):
    data = list(range(size))  
    if structure == "linked_list":
        ll = LinkedList()
        for num in data:
            ll.append(num)
        search_structure = ll
    else:
        arr = Array()
        for num in data:
            arr.append(num)
        search_structure = arr

    total_time = 0
    trials = 10 
    for _ in range(trials):
        target = np.random.choice(data) 
        start_time = time.time()
        search_structure.binary_search(target)
        total_time += time.time() - start_time

    return total_time / trials  

sizes = [1000, 2000, 4000, 8000]

linked_list_times = [measure_performance("linked_list", size) for size in sizes]
array_times = [measure_performance("array", size) for size in sizes]

plt.figure(figsize=(8, 6))
plt.plot(sizes, linked_list_times, marker='o', linestyle='-', label="Linked List (O(n))")
plt.plot(sizes, array_times, marker='s', linestyle='-', label="Array (O(log n))")
plt.xlabel("Input Size")
plt.ylabel("Average Search Time (seconds)")
plt.title("Binary Search Performance: Linked List vs Array")
plt.legend()
plt.grid()
plt.show()


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)

    print(linked_list.binary_search(3))
    print(linked_list.binary_search(7))

    arr = Array()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append(4)
    arr.append(5)
    arr.append(6)

    print(arr.binary_search(3))
    print(arr.binary_search(7))

    ''' 
        4.)
            The complexity of binary search for a Linked List like the one in the code
            above is O(log n). This is because arrays allow random access which means 
            that an item can be retrieved in O(1) time. However, for a linked list 
            Binary search, random access is not available which leaves the only way 
            to access a middle element is by traverising the entire list. This is a very
            time consuming process and has a time complexity of O(n). This causes the 
            overall complexity of the binary search on a linked list to be O(n).
    '''



