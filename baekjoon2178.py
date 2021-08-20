n, m = map(int,input().split())
s = []
queue = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    s.append(list(input()))
queue = [[0,0]]
s[0][0] = 1

# 지금 list를 str로 받았기 때문에 저게 있어야함..!
while queue:
    a , b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == '1':
            queue.append([x,y])
            s[x][y] = s[a][b] + 1

print(s)