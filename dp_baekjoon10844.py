# 문제
# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

n = int(input())

dp = [[0 for i in range(10)] for j in range(n)]

for i in range(1,10):
    dp[0][i] = 1

for i in range(1,n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n-1])%1000000000)

