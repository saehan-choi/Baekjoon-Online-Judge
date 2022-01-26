import sys
import heapq

n = int(input())
left_Heap = []
right_Heap= []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if i == 0:
        heapq.heappush(left_Heap, (-x,x))
        # print(left_Heap[0][1])
        
    elif left_Heap[0][1] < x:
        heapq.heappush(right_Heap, (-x,x))
        # print(left_Heap[0][1])
    else:
        heapq.heappush(left_Heap, (-x,x))
        # print(left_Heap[0][1])

    print(f'left_Heap : {left_Heap}')
    print(f'rigft_Heap : {right_Heap}')
    

    
    # print(right_Heap)

    # heap 자료구조 해당 index * 2 + 1 자식노드의 왼쪽
    # heap 자료구조 해당 index * 2 + 2 자식노드의 오른쪽
    # 0일때도 *2 적용

