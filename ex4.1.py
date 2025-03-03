"""
1. The best-case complexity will be when no elements in `li` are greater than 5 and the inner
loop is not used, so it will be O(n). The worst-case complexity will be when all elements are greater 
than 5 and the nested loops will make iterations, it will be O(n^2). The average-case complexity will be 
O(n^2) as numerous elements can trigger the inner loop.
"""

def processdata(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2