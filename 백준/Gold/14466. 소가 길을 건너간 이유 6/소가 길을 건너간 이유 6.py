"""
유형 : 다익스트라?
아이디어 : 
- 다익스트라로 한 정점에서 다른 정점으로 이동 가능한 거리를 구하자
- 다리를 거쳐야 하는 경우는 무한대의 가중치를 주자
주의
- 시간복잡도 : 소의 수 N * 각 소에 대한 다익스트라(ElogV=N^3)
    총 N^4 = 100^4 = 10^8 -> 가능?...
    - 다익스트라에서 pop한 원소가 target이라면 종료하여 시간 복잡도 줄이기?
    - 또는 결과를 저장하여 다시 다익스트라를 수행하지 않도록
0 0 0
0 1-1
    |
0 0-1
"""
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
def getNext(x, y, graph, roads):
    n = len(graph)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = []
    for direction in directions:
        nextX, nextY = map(sum, zip((x, y), direction))
        isValid = 0<=nextX<n and 0<=nextY<n
        isNotVisited = graph[nextX][nextY] if isValid else False
        isRoad = ((x, y), (nextX, nextY)) in roads
        if isValid and isNotVisited and not isRoad:
            res.append((nextX, nextY))
    return res
            
def BFS(start, n, roads):
    graph = [[1]*n for _ in range(n)]
    x, y = start
    graph[x][y] = 0
    q = deque([start])
    res = set()
    while q:
        x, y = q.popleft()
        for nextX, nextY in getNext(x, y, graph, roads):
            graph[nextX][nextY] = 0
            q.append((nextX, nextY))
    for x in range(n):
        for y in range(n):
            if graph[x][y]:
                res.add((x, y))
    # print(start, graph)
    # print(roads)
    # print('='*10)
    return res

n, k, r = map(int, input().split())
roads = set()
for _ in range(r):
    x1, y1, x2, y2 = map(lambda num: int(num)-1, input().split())
    roads.add(((x1, y1), (x2, y2)))
    roads.add(((x2, y2), (x1, y1)))
cows = []
for _ in range(k):
    x, y = map(lambda num: int(num)-1, input().split())
    cows.append((x, y))
dictionary = {}
answer = 0
for cow1, cow2 in combinations(cows, 2):
    if cow1 in dictionary:
        answer += 1 if cow2 in dictionary[cow1] else 0
    elif cow2 in dictionary:
        answer += 1 if cow1 in dictionary[cow2] else 0
    else:
        dictionary[cow1] = BFS(cow1, n, roads)
        answer += 1 if cow2 in dictionary[cow1] else 0
#     print(cow1, cow2, answer)
# print(dictionary)
print(answer)