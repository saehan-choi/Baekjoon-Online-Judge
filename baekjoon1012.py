T = int(input())
emp2 = []
def dfs(x,y):
    global cnt
    arr[y][x] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= M or ny >= N:
            continue
        if arr[ny][nx] == '1':
            dfs(nx,ny)
for i in range(T):
    M,N,K = map(int,input().split())
    dx = [-1,0,0,1]
    dy = [0,1,-1,0]
    arr = [[0]*M for i in range(N)]
    emp = []

    for i in range(K):
        x,y = map(int,input().split())
        arr[y][x] = '1'

    for i in range(M):
        for j in range(N):
            if arr[j][i]=='1':
                cnt = 0
                dfs(i,j)
                emp.append(cnt)
    emp2.append(len(emp))

for i in range(T):
    print(emp2[i])

