import sys
import heapq

n = int(input())
left_Heap = []
right_Heap= []

for i in range(n):
    x = int(sys.stdin.readline())
    heapq.heappush(left_Heap, x)

    print(left_Heap)
    # print(right_Heap)

    # heap 자료구조 해당 index * 2 + 1 자식노드의 왼쪽
    # heap 자료구조 해당 index * 2 + 2 자식노드의 오른쪽
    # 0일때도 *2 적용