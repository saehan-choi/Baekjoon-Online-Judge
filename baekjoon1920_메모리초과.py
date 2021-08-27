
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')

# 시간복잡도 매우줄어듦

# N1 = int(input())
# first_arr = list(set(map(int,input().split())))
# num_cnt = [0 for i in range(max(first_arr))]

# for i in range(len(first_arr)):
#     num_cnt[first_arr[i]-1] = first_arr[i]

# N2 = int(input())

# second_arr = list(set(map(int,input().split())))

# num_cnt_2 = [0 for i in range(max(second_arr))]

# for i in range(len(second_arr)):
#     num_cnt_2[second_arr[i]-1] = second_arr[i]

# for i in range(N1):
#     if num_cnt[i] == num_cnt_2[i]:
#         print(1)
#     else:
#         print(0)