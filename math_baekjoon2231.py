import sys
import time


N = int(sys.stdin.readline())

start = time.time()
for i in range(1,N+1):
    a = list(map(int,str(i)))
    # a = list(str(i))
    print(a)

print(f'{time.time()-start}s 소요됨')