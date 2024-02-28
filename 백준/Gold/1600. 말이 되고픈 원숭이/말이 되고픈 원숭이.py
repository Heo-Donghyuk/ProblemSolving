"""
유형:
아이디어:
- 점프를 k회 할 수 있다.
    - 큐에 집어 넣을 때 남은 점프 횟수를 함께 저장하자
        - cost, remainJump, x, y
- 방문 처리는 board를 1로(벽으로) 바꾸어버리자.
    => 안됨. 점프 횟수별 방문 여부를 따로 저장할 수 있어야 한다.
- isValid 함수를 정의하여 이동 가능 여부를 확인하자
주의:
-시간복잡도
-예외:
    - 도착점에 갈 수 없는 경우엔 -1을 출력하자
"""
import sys
input=sys.stdin.readline
from collections import deque

k = int(input())
w, h = map(int, input().split())
board = []
for _ in range(h):
    board.append(list(map(int, input().split())))
    
q = deque([(0, k, 0, 0)])
target = (h-1, w-1)
visited = [set() for _ in range(k+1)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
jumpDirection = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                 (2, 1), (2, -1), (-2, 1), (-2, -1)]
def BFS():
    while q:
        cost, remainJump, x, y = q.popleft()
        for d in direction:
            nx, ny = map(sum, zip((x, y), d))
            if (nx,ny)==target:
                return cost+1
            if 0<=nx<h and 0<=ny<w and (nx, ny) not in visited[remainJump] and board[nx][ny]!=1:
                q.append((cost+1, remainJump, nx, ny))
                visited[remainJump].add((nx, ny))
        if remainJump>0:
            for d in jumpDirection:
                nx, ny = map(sum, zip((x, y), d))
                if (nx,ny)==target:
                    return cost+1
                if 0<=nx<h and 0<=ny<w and (nx, ny) not in visited[remainJump-1] and board[nx][ny]!=1:
                    q.append((cost+1, remainJump-1, nx, ny))
                    visited[remainJump-1].add((nx, ny))
    return -1
print(0 if w==h==1 else BFS())