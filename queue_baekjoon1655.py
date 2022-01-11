import sys
import heapq

n = int(input())
left_Heap = []
right_Heap= []

for i in range(n):
    x = int(sys.stdin.readline())

    if i == 0:
        left_Heap.append(x)

    elif x > left_Heap[0]:
        heapq.heappush(right_Heap, x)

    elif x <= left_Heap[0]:
        heapq.heappush(left_Heap, x)

    print(left_Heap)
    print(right_Heap)
