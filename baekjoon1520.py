# 여행을 떠난 세준이는 지도를 하나 구하였다. 
# 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.
# 현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.
# 지도가 주어질 때 이와 같이 제일 왼쪽 위 지점에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로만 이동하는 경로의 개수를 구하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(1000000000)

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
            # print(f'x:{x} y:{y}')
            if x==N-1 and y ==M-1:
                cnt+=1            
            dfs(x,y)
        
dfs(0,0)
print(cnt)