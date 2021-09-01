N = int(input())

connection_ = int(input())



visit = [0 for i in range(N+1)]
s = [[0]*(N+1) for i in range(N+1)]

for i in range(connection_):
    x,y = map(int,input().split())
    s[x][y] = 1
    s[y][x] = 1

def dfs(v):
    visit[v] = 1
    for i in range(1,N+1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)

dfs(1)
print(sum(visit)-1)