
# inp = int(input())
# arr = []
# for i in range(inp):
#     k = int(input())
#     if k == 0:
#         if arr:
#             arr.sort()
#             print(arr.pop())    
#         else:
#             print(0)
#     else:
#         arr.append(k)
# 시간 out

import sys
import heapq as hq

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)
    # print(heap)
    # 배열을 직접보면서 실험해보고 싶으면 print(0)지우고 print(heap) 살려서 배열확인하면 이해할수있음
    # this code from at https://mong9data.tistory.com/101