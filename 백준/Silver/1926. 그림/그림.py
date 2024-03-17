import sys
input = sys.stdin.readline
from collections import deque
from itertools import product

n, m = map(int, input().split())
table = []
answer = [0, 0]
for _ in range(n):
    table.append(list(map(int, input().split())))

q = deque()
for i, j in product(range(n), range(m)):
    if table[i][j]:
        q.append((i, j))
        answer[0]+=1
        temp = 1
        table[i][j] = 0
        while q:
            x, y = q.popleft()
            for addX, addY in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x+addX, y+addY
                if 0<=nx<n and 0<=ny<m and table[nx][ny]:
                    q.append((nx, ny))
                    table[nx][ny] = 0
                    temp+=1
        answer[1] = max(temp, answer[1])
    
print(answer[0])
print(answer[1])