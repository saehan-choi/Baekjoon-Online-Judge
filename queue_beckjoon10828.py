from collections import deque
import sys
que = deque()

N = int(sys.stdin.readline())

for i in range(N):
    control = sys.stdin.readline().split()
    
    if control[0] == 'push':
        que.appendleft(int(control[1]))

    elif control[0] == 'top':
        if que:
            print(que[0])
        else:
            print(-1)

    elif control[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)

    elif control[0] == 'size':
        print(len(que))

    elif control[0] == 'empty': 
        if que:
            print(0)
        else:
            print(1)