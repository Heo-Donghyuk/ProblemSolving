import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

inf = 10**9
def dijkstra(start, graph, nodeNum):
    result = [inf]*(nodeNum+1)
    result[start]=0
    q = [(0, start)]
    while q:
        cost, node = heappop(q)
        if result[node]<cost:
            continue
        else:
            for nextNode, nextCost in graph[node].items():
                newCost = cost+nextCost
                if result[nextNode]>newCost:
                    result[nextNode]=newCost
                    heappush(q, (newCost, nextNode))
    return result[1:]

v, e = map(int, input().split())
start = int(input())
graph = defaultdict(dict)
for _ in range(e):
    node1, node2, cost = map(int, input().split())
    if node2 not in graph[node1] or graph[node1][node2]>cost:
        graph[node1][node2]=cost
for n in dijkstra(start, graph, v):
    print(str(n) if n!=inf else 'INF')
