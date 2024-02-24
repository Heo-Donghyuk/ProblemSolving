import sys
from collections import defaultdict
from heapq import *
input = sys.stdin.readline
INF = 10**9

def dijkstra(start, graph, nodeNum):
    res = [INF]*(nodeNum+1)
    res[start]=0
    q = [(0, start)]
    while q:
        cost, curNode = heappop(q)
        if cost>res[curNode]:
            continue
        for nextNode, nextCost in graph[curNode].items():
            newCost = cost+nextCost
            if res[nextNode]>newCost:
                res[nextNode]=newCost
                heappush(q, (newCost, nextNode))
    return res[1:]

v, e = map(int, input().split())
start = int(input())
graph = defaultdict(dict)
for _ in range(e):
    node1, node2, cost = map(int, input().split())
    if node2 not in graph[node1] or graph[node1][node2]>cost:
        graph[node1][node2]=cost
    
for dist in dijkstra(start, graph, v):
    print(dist if dist!=INF else 'INF')
