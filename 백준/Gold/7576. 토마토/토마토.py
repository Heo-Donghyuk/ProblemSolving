"""
유형: BFS
아이디어:
- BFS로 토마토를 익게 만들자
    - BFS가 완료된 후 0인(익지않은) 토마토가 하나라도 있다면 -1을 출력하자
    - 아니라면 bfs의 결과를 출력하자
주의:
-시간복잡도
-예외:
    - 인덱스 주의
    - 익은 토마토가 2개 이상일 수 있나?
    - 익은 토마토가 없을 수 있나?
"""
import sys
input = sys.stdin.readline
from collections import deque

def isValid(x, y):
    if 0<=x<n and 0<=y<m and board[x][y]==0:
        return True
    return False

m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque()
cost, remain = 0, 0
for x in range(n):
    for y in range(m):
        if board[x][y]==1:
            q.append((0, x, y))
        elif board[x][y]==0:
            remain+=1
# BFS
while q:
    cost, x, y = q.popleft()
    for d in direction:
        nx, ny = map(sum, zip((x, y), d))
        if isValid(nx, ny):
            board[nx][ny]=-1
            remain-=1
            q.append((cost+1, nx, ny))
    
# 안익은 토마토가 있는지 확인
print(cost if not remain else -1)