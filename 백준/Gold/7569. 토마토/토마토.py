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

def sol():
    m, n, h = map(int, input().split())
    board = [[[0]*m for _ in range(n)] for __ in range(h)]
    q = deque()
    cost, remain = 0, 0
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
        if 0<=x+1<h and 0<=y<n and 0<=z<m and board[x+1][y][z]==0:
            board[x+1][y][z]=-1
            remain-=1
            q.append((cost+1, x+1, y, z))
        if 0<=x-1<h and 0<=y<n and 0<=z<m and board[x-1][y][z]==0:
            board[x-1][y][z]=-1
            remain-=1
            q.append((cost+1, x-1, y, z))
        if 0<=x<h and 0<=y+1<n and 0<=z<m and board[x][y+1][z]==0:
            board[x][y+1][z]=-1
            remain-=1
            q.append((cost+1, x, y+1, z))
        if 0<=x<h and 0<=y-1<n and 0<=z<m and board[x][y-1][z]==0:
            board[x][y-1][z]=-1
            remain-=1
            q.append((cost+1, x, y-1, z))
        if 0<=x<h and 0<=y<n and 0<=z+1<m and board[x][y][z+1]==0:
            board[x][y][z+1]=-1
            remain-=1
            q.append((cost+1, x, y, z+1))
        if 0<=x<h and 0<=y<n and 0<=z-1<m and board[x][y][z-1]==0:
            board[x][y][z-1]=-1
            remain-=1
            q.append((cost+1, x, y, z-1))
        else:
            continue
    # 익지 않은 토마토 판별
    print(-1 if remain else cost)
sol()