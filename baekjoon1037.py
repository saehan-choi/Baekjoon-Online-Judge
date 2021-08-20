N = int(input())

leaknum = list(map(int, input().split()))

print(max(leaknum)*min(leaknum))