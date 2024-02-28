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
from itertools import product
from collections import deque

def isValid(x, y, z, board):
    h, n, m = len(board), len(board[0]), len(board[0][0])
    if 0<=x<h and 0<=y<n and 0<=z<m and board[x][y][z]==0:
        return True
    return False
    

m, n, h = map(int, input().split())
board = [[[0]*m for _ in range(n)] for __ in range(h)]
q = deque()
cost, remain = 0, 0
for i, j in product(range(h), range(n)):
    for k, val in enumerate(map(int, input().split())):
        if val==1:
            q.append((0, i, j, k))
        elif val==0:
            remain+=1
        board[i][j][k] = -1 if val else 0

direction = [(0, 0, 1), (0, 1, 0), (1, 0, 0),
             (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
# BFS        
while q:
    cost, x, y, z = q.popleft()
    for d in direction:
        nx, ny, nz = map(sum, zip((x, y, z), d))
        if isValid(nx, ny, nz, board):
            board[nx][ny][nz]=-1
            remain-=1
            q.append((cost+1, nx, ny, nz))
# 익지 않은 토마토 판별
if remain!=0:
    cost=-1
print(cost)