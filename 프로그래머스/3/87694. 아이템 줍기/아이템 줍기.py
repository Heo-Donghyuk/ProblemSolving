from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*101 for _ in range(101)]
    rectangle = [[a*2, b*2, c*2, d*2] for a, b, c, d in rectangle]
    for lowX, lowY, highX, highY in rectangle:
        for x in range(lowX, highX+1):
            for y in range(lowY, highY+1):
                if (x in (lowX, highX) or y in (lowY, highY)) and board[x][y]!=-1:
                    board[x][y]=1
                else:
                    board[x][y]=-1
    q = deque([(0, characterX*2, characterY*2)])
    visited = set()
    while q:
        dist, x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y)==(itemX*2, itemY*2):
            return dist//2
        for addX, addY in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nextX, nextY = x+addX, y+addY
            if 1<nextX<=100 and 1<nextY<=100 and board[nextX][nextY]==1:
                q.append((dist+1, nextX, nextY))
    return -1
import bisect
help(bisect)