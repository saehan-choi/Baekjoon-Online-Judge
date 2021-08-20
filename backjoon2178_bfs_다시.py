n , m = map(int,input().split())

s = []
# queue = []

dx = [0,0,1,-1] 
dy = [1,-1,0,0]

for i in range(n):
    s.append(list(input()))

s[0][0] = 1
queue = [[0,0]]

while queue:
    a , b = queue[0][0], queue[0][1]
    del queue[0]

    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == '1':
            queue.append([x,y])
            # s[a][b] + 1  ㅇㅈ ㅇㅈㅇㅈㅇㅈ 이거다
            s[x][y] = s[a][b] + 1

print(s[n-1][m-1])