import time
import matplotlib.pyplot as plt


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def get_size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def get_element_at_pos(self, pos):
        temp = self.head
        for _ in range(pos):
            temp = temp.next
        return temp

    def reverse_given(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # Optimized reverse function (O(n))
    def reverse_optimized(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


def time_reverse_methods(n, iterations=100):
    given_times = []
    optimized_times = []

    for _ in range(iterations):
        ll = LinkedList()
        for i in range(n):
            ll.insert_head(i)

        start = time.time()
        ll.reverse_given()
        given_times.append(time.time() - start)

        ll = LinkedList()
        for i in range(n):
            ll.insert_head(i)

        start = time.time()
        ll.reverse_optimized()
        optimized_times.append(time.time() - start)

    return sum(given_times) / iterations, sum(optimized_times) / iterations

sizes = [1000, 2000, 3000, 4000]
given_results = []
optimized_results = []

for size in sizes:
    given_time, optimized_time = time_reverse_methods(size)
    given_results.append(given_time)
    optimized_results.append(optimized_time)

plt.figure(figsize=(8,6))
plt.plot(sizes, given_results, marker='o', label='Given Reverse (O(n^2))')
plt.plot(sizes, optimized_results, marker='s', label='Optimized Reverse (O(n))')
plt.xlabel('Number of Elements')
plt.ylabel('Average Time (seconds)')
plt.title('Performance Comparison: Given vs Optimized Reverse')
plt.legend()
plt.grid(True)
plt.show()
