N,M = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,1,-1]
arr = []

cnt = 0

for i in range(N):
    arr.append(list(map(int,input().split())))

def dfs(a,b):
    global cnt
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]

        if 0 <= x < N and 0 <= y < M and arr[a][b] > arr[x][y]:
            print(f'x:{x} y:{y}')
            if x==N-1 and y ==M-1:
                cnt+=1            
            dfs(x,y)
        
dfs(0,0)
print(cnt)