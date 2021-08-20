N = int(input())
b = [list(input()) for i in range(N)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
arr = []

def dfs(x,y):
    global cnt
    b[x][y] = '0'
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if b[nx][ny] == '1':
            
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if b[i][j] == '1':
            cnt = 0
            dfs(i,j)
            arr.append(cnt)
                
arr.sort()
len_arr = len(arr)
print(len_arr)

for i in range(len_arr):
    print(arr[i])