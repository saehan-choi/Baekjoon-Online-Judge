import sys
T = int(sys.stdin.readline())

arr = [1, 1, 1, 2, 2, 3, 4, 5]
empty = []

for i in range(T):
    N = int(sys.stdin.readline())

    if N >= 8:
        for i in range(8,N):
            arr.append(arr[i-5]+arr[i-1])
        empty.append(arr[N-1])

    elif N < 8:
        empty.append(arr[N-1])
    
    arr = [1, 1, 1, 2, 2, 3, 4, 5]

for i in range(T):
    print(empty[i])


# import sys
# from collections import deque

# T = int(sys.stdin.readline())

# arr = [1, 1, 1, 2, 2, 3, 4, 5]
# queue = deque()
# empty = []

# for i in range(T):
#     N = int(sys.stdin.readline())

#     if N >= 8:
#         for i in range(8,N):
#             arr.append(arr[i-5]+arr[i-1])
#         queue.append(arr[N-1])

#     elif N < 8:
#         queue.append(arr[N-1])
    
#     arr = [1, 1, 1, 2, 2, 3, 4, 5]

# for i in range(T):
#     print(queue.popleft())