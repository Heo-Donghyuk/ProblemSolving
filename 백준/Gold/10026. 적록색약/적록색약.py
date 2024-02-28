"""
유형: BFS/DFS
아이디어:
- BFS로 이동 가능한 칸을 탐색하자
    - isValid 함수를 만들어 이동 가능 여부를 판단하자
        - isValid는 R,G,B에 따른 이동 가능 여부를 판단할 수 있도록 구현하자
- 적록 색약의 경우 R과 G의 구분이 없다.
    - isValid 함수 내부에서 구분이 없도록 로직 처리를 해주거나
    - board에서 G를 R로 대체하자
주의:
-시간복잡도
-예외
    - 적록색약의 경우 R, G의 구분이 없다.
"""
import sys
input = sys.stdin.readline
from collections import deque

def BFS(x, y, target, board):
    n = len(board)
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for d in direction:
            nx, ny = map(sum, zip((x, y), d))
            if isValid(nx, ny, target, board):
                board[nx][ny]=0
                q.append((nx, ny))

def isValid(x, y, target, board):
    n = len(board)
    if 0<=x<n and 0<=y<n and board[x][y]==target:
        return True
    return False

n = int(input())
board = []
for i in range(n):
    board.append(list(input()))
boardRG = [list(map(lambda x: 'R' if x=='G' else x, arr)) for arr in board]

answer = [0, 0]
for x in range(n):
    for y in range(n):
        if board[x][y]!=0:
            target = board[x][y]
            board[x][y]=0
            BFS(x, y, target, board)
            answer[0]+=1
        if boardRG[x][y]!=0:
            target = boardRG[x][y]
            boardRG[x][y]=0
            BFS(x, y, target, boardRG)
            answer[1]+=1
            
print(answer[0], answer[1])