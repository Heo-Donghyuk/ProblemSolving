"""
유형: DFS/BFS
아이디어:
- 3차원 테이블을 만들고
- 거기서 BFS/DFS
주의:
-시간복잡도
-예외:
    - 최초 익은 토마토가 여러개일 수 있다.
"""
import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
board = [[[0]*m for _ in range(n)] for __ in range(h)]
q = deque()
cost, remain = 0, 0
direction = [(0, 0, 1), (0, 1, 0), (1, 0, 0),
             (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
for i in range(h):
    for j in range(n):
        for k, val in enumerate(map(int, input().split())):
            if val==0:
                remain+=1
                board[i][j][k] = 0
            elif val==-1:
                board[i][j][k] = -1
            else:
                q.append((0, i, j, k))
                board[i][j][k] = -1

# BFS        
while q:
    cost, x, y, z = q.popleft()
    for d in direction:
        if 0<=x+d[0]<h and 0<=y+d[1]<n and 0<=z+d[2]<m and board[x+d[0]][y+d[1]][z+d[2]]==0:
            board[x+d[0]][y+d[1]][z+d[2]]=-1
            remain-=1
            q.append((cost+1, x+d[0], y+d[1], z+d[2]))
# 익지 않은 토마토 판별
print(-1 if remain else cost)