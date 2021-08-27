import sys
from collections import Counter

N = int(sys.stdin.readline())
A,B = [0 for i in range(N)], [0 for i in range(N)]
emp = []
emp2 = []
for i in range(N):
    # pass
    A[i], B[i] = map(int,input().split())

for i in range(N):
    for j in range(N):
        if i == j:
            pass
        elif A[i]>A[j] and B[i]>B[j]:
            emp.append(i)

cnt = Counter(emp)
cnt = cnt.most_common()

