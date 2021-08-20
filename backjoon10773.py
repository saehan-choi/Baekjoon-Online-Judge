import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for i in range(N):
    inp = int(sys.stdin.readline())
    
    if inp == 0:
        que.popleft()
    else:
        que.appendleft(inp)

print(sum(que))