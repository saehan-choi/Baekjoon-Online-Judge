import heapq
import sys
n = int(input())
arr = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(arr,x)
    else:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)