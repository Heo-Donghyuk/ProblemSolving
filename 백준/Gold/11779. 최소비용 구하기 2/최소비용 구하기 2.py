import sys
input=sys.stdin.readline
from heapq import *

def dijkstra(start):
    res = [10**9]*(n+1)
    q = [(0, start)]
    route = [[] for _ in range(n+1)]
    while q:
        cost, cur = heappop(q)
        if cost>res[cur]:
            continue
        for nextNode, nextCost in graph[cur].items():
            totalCost = cost+nextCost
            if res[nextNode]>totalCost:
                res[nextNode]=totalCost
                heappush(q, (totalCost, nextNode))
                
                route[nextNode] = route[cur]+[nextNode]
    return [res, route]

n, m = int(input()), int(input())
graph = {i:{i:0} for i in range(n+1)}
for _ in range(m): # 그래프 초기화
    node1, node2, cost = map(int, input().split())
    if node2 not in graph[node1] or graph[node1][node2]>cost:
        graph[node1][node2] = cost



start, end = map(int, input().split())
dist, route = dijkstra(start)
print(dist[end])
print(len(route[end]))
print(' '.join(map(str, route[end])))