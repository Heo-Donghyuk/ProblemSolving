"""
유형: BFS
아이디어:
- BFS를 이용하자
    - 벽을 1회 부술 수 있다 -> 남은 벽을 부술 수 있는 횟수를 큐에 함께 포함하자
    - 다음 좌표가 유효하고
        - 벽이 아니라면
            - 큐에 cost+1하여 추가
        - 벽이고 벽을 부술 수 있는 횟수가 남아있다면
            - 큐에 cost+1, remain-1하여 추가
    - 방문 처리:
        - 벽을 부수고 도착한 좌표와 부수지 않고 도착한 좌표의 방문 처리를 따로 해야 한다.
        - 벽을 부수고 더 빨리 어떤 좌표에 도달했다 하더라도 이후에 다른 벽을 만나면 목적지에 도달할 수 없다.
            그래서 벽을 부수고 도달한 좌표는 따로 처리해야 한다.
주의:
- 예외
    - 벽을 1회 부술 수 있다.
    - n, m이 1일 수 있다.
    - 시작, 끝 칸을 포함한다.
"""
import sys
input=sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [[int(i) for i in input().strip()] for _ in range(n)]
visited = [[[0]*(m+1) for _ in range(n+1)], [[0]*(m+1) for _ in range(n+1)]]
q = deque([(1, 1, 0, 0)])
def BFS():
    while q:
        cost, remain, x, y = q.popleft()
        if (x, y)==(n-1, m-1):
            return cost
        for addX, addY in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x+addX, y+addY
            if 0<=nx<n and 0<=ny<m and visited[remain][nx][ny]==False:
                if board[nx][ny]==0: # 벽이 아니라면
                    q.append((cost+1, remain, nx, ny))
                    visited[remain][nx][ny]=True
                elif remain: # 벽이고 부술 수 있다면
                    q.append((cost+1, 0, nx, ny))
                    visited[0][nx][ny]=True
    return -1
print(BFS())