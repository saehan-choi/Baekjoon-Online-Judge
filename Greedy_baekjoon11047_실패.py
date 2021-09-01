# 준규가 가지고 있는 동전은 총 N종류이고, 
# 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
import sys

N, K = map(int,sys.stdin.readline().split())
arr = []
arr2 = []
cnt = 0
for i in range(N):
    arr.append(int(sys.stdin.readline()))

for i in range(N):
    if K//arr[i]>1:
        arr2.append(arr[i])

while True:
    K = K - max(arr2)
    cnt += 1
    if 0< K/max(arr2) <1:
        while True:
            del arr2[-1]
            if 1<K/max(arr2):
                break
    if K == 0:
        break

print(cnt)
