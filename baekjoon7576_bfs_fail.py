N , M = map(int,input().split())

s = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(M):
    s.append(list(map(str, input().split())))


queue = [[M,N]]
# s[0][0] = 1
cnt = 0
while queue:
    a , b = queue[0][0], queue[0][1]
    # print('---------------')
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < M and 0 <= y < N and s[x][y] == '0':
            queue.append([x,y])
            s[x][y] = '1'
    print(s)
    cnt+=1
    print(cnt)

print(cnt)
print(s)

