"""
BFS로 다시 풀어보기
아이디어:
- 이동할 수 있는 다음 좌표를 큐에 집어넣자
    - 큐에서 pop할 때 마다 면적을 1씩 늘리자.
"""
import sys
input = sys.stdin.readline
from collections import deque
from itertools import product

def BFS(x, y, board):
    res, board[x][y]= 1, 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for d in direction:
            nextX, nextY = map(sum, zip((x, y), d))
            if isValid(nextX, nextY, board):
                q.append((nextX, nextY))
                board[nextX][nextY]=0
                res+=1
    return res

def isValid(x, y, board):
    n, m = len(board), len(board[0])
    if 0<=x<n and 0<=y<m and board[x][y]:
        return True
    return False
                
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
count, area = 0, 0
for x, y in product(range(n), range(m)):
    if board[x][y]:
        area = max(area, BFS(x, y, board))
        count+=1
print(count)
print(area)