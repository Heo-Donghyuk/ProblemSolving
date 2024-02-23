"""
소요시간 : 30분, 아이디어 10분 구현 15분, 트러블슈팅 5분
유형: DP? 다익스트라?
아이디어:
- DP : 우하로만 이동 가능한 경우에는 가능, 하지만 상하좌우로 이동 가능하므로 조금 더 생각할 필요가 있음
- 다익스트라 : ElogV -> N^3 -> 가능
주의:
- 시간복잡도
- 조건
- 예외
"""
from heapq import heappush, heappop

def dijkstra(start, graph):
    INF = 10**9
    result = [[INF]*len(graph[0]) for _ in range(len(graph))]
    result[start[0]][start[1]]=graph[start[0]][start[1]]
    q = [(graph[start[0]][start[1]], start)]
    while q:
        cost, coord = heappop(q)
        x, y = coord
        if cost>result[x][y]:
            continue
        for nextX, nextY in getNext(coord, graph):
            nextCost = graph[nextX][nextY]
            newCost = cost+nextCost
            if result[nextX][nextY]>newCost:
                result[nextX][nextY] = newCost
                heappush(q, (newCost, (nextX, nextY)))
    return result

def getNext(coord, graph):
    n, m = len(graph), len(graph[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = []
    for direction in directions:
        nextX, nextY = map(sum, zip(coord, direction))
        if 0<=nextX<n and 0<=nextY<m:
            res.append((nextX, nextY))
    return res
    
count = 0
while True:
    count += 1
    n = int(input())
    if n==0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
        
    result = dijkstra((0,0), graph)
    print(f'Problem {count}: {result[-1][-1]}')
    
    