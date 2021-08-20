# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 
# 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

C = int(input())
cnt = 0
arr = []
for i in range(C):
    nums = list(map(int, input().split()))
    total=(sum(nums[1:])/nums[0])
    
    for j in range(1,nums[0]+1):
        if nums[j]>total:
            cnt+=1
    arr.append("{:.3f}%".format(round(cnt/nums[0]*100,3)))
    cnt=0

for i in range(C):
    print(arr[i])

# import sys
# input = sys.stdin.readline

# test_case = int(input())

# for _ in range(test_case):
#     data = input().strip().split(' ')
#     scores = list(map(float, data[1:]))
#     average = sum(scores) / len(scores)

#     above = 0
#     for score in scores:
#         if score > average:
#             above += 1

#     print(f'{(above/len(scores))*100:.3f}%')